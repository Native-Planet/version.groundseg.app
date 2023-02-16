#### Native Planet software version server

Serves a JSON blob with current version information for all software.

Gets updated by authenticated webhook called by Jenkins build jobs.

Stores data in sqlite db.

```json
{
"groundseg":
    {
        "latest": {
            "groundseg": {
                "major": 1,
                "minor": 0, 
                "patch": 8,
                "amd64_url": "https://bin.infra.native.computer/groundseg_amd64_latest",
                "arm64_url": "https://bin.infra.native.computer/groundseg_arm64_latest",
                "amd64_sha256": "24c09a8b94207c5530657960f67d151d311f00d934f21d4748bd3c6256699fb9",
                "arm64_sha256": "2a2ee6a79b165d5266da711dda50cbda88ff0c9745917d48bb2ce0662ad2f43c"
            },
            "webui": {
                "repo": "registry.hub.docker.com/nativeplanet/groundseg-webui",
                "tag": "latest",
                "sha256": "5c6f205787342525daaa3b60407c534a1260824644ebb167c6e4d90247d5b6f7"
            },
            "vere": {
                "repo": "registry.hub.docker.com/nativeplanet/urbit",
                "tag": "v1.20",
                "sha256": "e3d1624382ebb35355c9560558cdfa170ff1950bb8651ab5536454b54050b451"
            },
            "minio": {
                "repo": "registry.hub.docker.com/minio/minio",
                "tag": "latest",
                "sha256": "827e74d04dcdd6125c765f56dcf0bde7f057ecf693789d04e205bad7db630f8a"
            },
            "wireguard": {
                "repo": "registry.hub.docker.com/linuxserver/wireguard",
                "tag": "latest",
                "sha256": "0b2f7166795ef50e62bf2e8531f5dec4d1671777c586878c33cc4f65e961502c"
            }
        },
        "edge": {
            "groundseg": {
                "major": 1,
                "minor": 0, 
                "patch": 8,
                "amd64_url": "https://bin.infra.native.computer/groundseg_amd64_edge",
                "arm64_url": "https://bin.infra.native.computer/groundseg_arm64_edge",
                "amd64_sha256": "24c09a8b94207c5530657960f67d151d311f00d934f21d4748bd3c6256699fb9",
                "arm64_sha256": "2a2ee6a79b165d5266da711dda50cbda88ff0c9745917d48bb2ce0662ad2f43c"
            },
            "webui": {
                "repo": "registry.hub.docker.com/nativeplanet/groundseg-webui",
                "tag": "edge",
                "sha256": "226335a6c3b41046cd4122a1c8cddd66b75ea76efca39de7b04be684ea2354ec"
            },
            "vere": {
                "repo": "registry.hub.docker.com/nativeplanet/urbit",
                "tag": "v1.20",
                "sha256": "e3d1624382ebb35355c9560558cdfa170ff1950bb8651ab5536454b54050b451"
            },
            "minio": {
                "repo": "registry.hub.docker.com/minio/minio",
                "tag": "latest",
                "sha256": "827e74d04dcdd6125c765f56dcf0bde7f057ecf693789d04e205bad7db630f8a"
            },
            "wireguard": {
                "repo": "registry.hub.docker.com/linuxserver/wireguard",
                "tag": "latest",
                "sha256": "0b2f7166795ef50e62bf2e8531f5dec4d1671777c586878c33cc4f65e961502c"
            }
        }
    }
}
```