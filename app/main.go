package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log/slog"
	"net/http"
	"os"
	"strconv"
	"strings"
	"version/db"
	"version/structs"

	"github.com/gorilla/mux"
)

var (
	authkey     = os.Getenv("AUTHKEY")
	logger      = slog.New(slog.NewJSONHandler(os.Stdout, nil))
	versionData *structs.Version
)

func init() {
	versionStr, err := db.Get()
	if err != nil {
		logger.Error(fmt.Sprintf("%v", err))
	}
	if versionStr == "" {
		content, err := ioutil.ReadFile("default_vals.json")
		if err != nil {
			panic("No default values provided")
		}
		if err := json.Unmarshal([]byte(content), &versionData); err != nil {
			panic("Invalid default values provided")
		}
	} else {
		if err := json.Unmarshal([]byte(versionStr), &versionData); err != nil {
			panic("Invalid version data saved")
		}
	}
}

func main() {
	authkey = os.Getenv("AUTHKEY")
	r := mux.NewRouter()
	r.HandleFunc("/", getConf).Methods("GET")
	r.HandleFunc("/modify/groundseg/{channel}/{software}/{key}/{value}", updConf).Methods("PUT")
	r.Use(authMiddleware)
	http.ListenAndServe("0.0.0.0:8090", r)
}

func getConf(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(versionData)
}

func updConf(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	channel := vars["channel"]
	software := vars["software"]
	key := vars["key"]
	val := vars["value"]
	var incomingValue interface{}
	if val == "payload" {
		bodyData := make(map[string]interface{})
		err := json.NewDecoder(r.Body).Decode(&bodyData)
		if err != nil {
			http.Error(w, "Invalid payload", http.StatusBadRequest)
			return
		}
		incomingValue = bodyData["value"]
	} else {
		incomingValue = val
	}
	dataMap := make(map[string]interface{})
	jsonData, err := json.Marshal(versionData)
	if err != nil {
		http.Error(w, "Failed to marshal versionData", http.StatusInternalServerError)
		return
	}
	err = json.Unmarshal(jsonData, &dataMap)
	if err != nil {
		http.Error(w, "Failed to unmarshal into dataMap", http.StatusInternalServerError)
		return
	}
	groundseg, ok := dataMap["groundseg"].(map[string]interface{})
	if !ok {
		http.Error(w, "Invalid structure", http.StatusInternalServerError)
		return
	}
	channelData, ok := groundseg[channel].(map[string]interface{})
	if !ok {
		http.Error(w, "Invalid channel", http.StatusBadRequest)
		return
	}
	softwareData, ok := channelData[software].(map[string]interface{})
	if !ok {
		http.Error(w, "Invalid software", http.StatusBadRequest)
		return
	}
	switch key {
	case "minor", "major", "patch":
		iVal, err := strconv.Atoi(fmt.Sprintf("%v", incomingValue))
		if err != nil {
			http.Error(w, "Invalid integer value", http.StatusBadRequest)
			return
		}
		softwareData[key] = iVal
	default:
		softwareData[key] = incomingValue
	}
	jsonData, err = json.Marshal(dataMap)
	if err != nil {
		http.Error(w, "Failed to marshal dataMap", http.StatusInternalServerError)
		return
	}
	err = json.Unmarshal(jsonData, &versionData)
	if err != nil {
		http.Error(w, "Failed to unmarshal into versionData", http.StatusInternalServerError)
		return
	}
	blob, err := json.Marshal(versionData)
	if err != nil {
		http.Error(w, "Error encoding data", http.StatusInternalServerError)
		return
	}
	if err = db.Update(string(blob)); err != nil {
		http.Error(w, "Error saving to database", http.StatusInternalServerError)
		return
	}
	logger.Info(fmt.Sprintf("Updated values: %+v", vars))
	w.WriteHeader(http.StatusOK)
	w.Write([]byte("Updated successfully"))
}

func authMiddleware(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		if strings.HasPrefix(r.URL.Path, "/modify") {
			auth := r.Header.Get("X-Api-Key")
			fwdIP := r.Header.Get("X-Forwarded-For")
			if auth != authkey {
				logger.Info(fmt.Sprintf("Failed auth request from %s", fwdIP))
				http.Error(w, `{"error": "Failed auth"}`, http.StatusForbidden)
				return
			}
		}
		next.ServeHTTP(w, r)
	})
}

func capitalizeFirst(s string) string {
	if s == "" {
		return ""
	}
	return strings.ToUpper(string(s[0])) + s[1:]
}
