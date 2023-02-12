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
            "patch": 7,
            "amd64_url": "https://asd.coma/sdasd_x64",
            "arm64_url": "https://asd.com/asdasd_arm"
            "checksum": "234erf3"
        },
        "vere": {
            "repo": "registry.hub.docker.com/nativeplanet/urbit",
            "tag": "v1.18",
            "checksum": "23rfew3"
        },
        "minio": {
            "repo": "registry.hub.docker.com/minio/minio",
            "tag": "whatever"
            "checksum": "234rf234fwe"
        },
        "wireguard": {
            "repo": "registry.hub.docker.com/linuxserver/wireguard",
            "tag": "blah",
            "checksum": "3254asdr23"
        }
    },
    "edge": {
        "groundseg": {
            "major": 1,
            "minor": 0, 
            "patch": 8,
            "url": "https://asdasd",
            "checksum": "234erf3"
        },
        "vere": {
            "repo": "registry.hub.docker.com/nativeplanet/urbit",
            "tag": "v1.19",
            "checksum": "23rfew3"
        },
        "minio": {
            "repo": "registry.hub.docker.com/minio/minio",
            "tag": "whatever"
            "checksum": "234rf234fwe"
        },
        "wireguard": {
            "repo": "registry.hub.docker.com/linuxserver/wireguard",
            "tag": "blah",
            "checksum": "3254asdr23"
        }
    },
}
```