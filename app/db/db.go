package db

import (
	"database/sql"
	"time"

	_ "github.com/glebarez/go-sqlite"
)

func init() {
	db, err := sql.Open("sqlite", "/data/db.sq3")
	if err != nil {
		panic(err)
	}
	defer db.Close()
	_, err = db.Exec(`
		CREATE TABLE IF NOT EXISTS version (
			id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
			blob TEXT NULL,
			timestamp TIMESTAMP NULL
		);
	`)
	if err != nil {
		panic(err)
	}
}

func getTime() string {
	currentTime := time.Now()
	return currentTime.Format("2006-01-02 15:04:05")
}

func Get() (string, error) {
	db, err := sql.Open("sqlite", "/data/db.sq3")
	if err != nil {
		return "", err
	}
	defer db.Close()
	var result string
	query := `SELECT blob FROM version ORDER BY timestamp DESC LIMIT 1`
	err = db.QueryRow(query).Scan(&result)
	if err != nil {
		if err == sql.ErrNoRows {
			return "", nil
		}
		return "", err
	}
	return result, nil
}

func Update(blob string) error {
	db, err := sql.Open("sqlite", "/data/db.sq3")
	defer db.Close()
	if err != nil {
		return err
	}
	tx, err := db.Begin()
	if err != nil {
		return err
	}
	stmt, err := tx.Prepare("INSERT INTO version(blob, timestamp) values(?, ?)")
	if err != nil {
		return err
	}
	defer stmt.Close()
	_, err = stmt.Exec(blob, getTime())
	if err != nil {
		return err
	}
	tx.Commit()
	return nil
}