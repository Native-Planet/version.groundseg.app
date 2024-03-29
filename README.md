#### Native Planet software version server

Serves a JSON blob with current version information for all software.

Gets updated by authenticated webhook called by Jenkins build jobs.

Caches data in sqlite db.

```json
{
  "groundseg": {
    "canary": {
      "groundseg": {
        "amd64_sha256": "746baf4406aa87b04ffeb3184a72dd1b4f26f90f844b1954e56ea680155df799",
        "amd64_url": "https://files.native.computer/bin/groundseg_amd64_v1.4.3_latest",
        "arm64_sha256": "f84a6cf87981091e0168492dd3717aa61579ecf6ca24c7c6e0d72e7049cadcad",
        "arm64_url": "https://files.native.computer/bin/groundseg_arm64_v1.4.3_latest",
        "major": 1,
        "minor": 4,
        "patch": 3
      },
      "manual": {
        "amd64_sha256": "23ecf8748d797bc6e450aa69523f3ca9377dd0657ea652ad3f1c3521ad65b4cb",
        "arm64_sha256": "006864e0199eae9f773dd93c54bc395ea6eb28f02e43f9105338dda53543b224",
        "repo": "registry.hub.docker.com/nativeplanet/groundseg-manual",
        "tag": "latest"
      },
      "minio": {
        "amd64_sha256": "f6a3001a765dc59a8e365149ade0ea628494230e984891877ead016eb24ba9a9",
        "arm64_sha256": "567779c9f29aca670f84d066051290faeaae6c3ad3a3b7062de4936aaab2a29d",
        "repo": "registry.hub.docker.com/minio/minio",
        "tag": "latest"
      },
      "miniomc": {
        "amd64_sha256": "6ffd76764e8ca484de12c6ecaa352db3d8efd5c9d44f393718b29b6600e0a559",
        "arm64_sha256": "6825aecd2f123c9d4408e660aba8a72f9e547a3774350b8f4d2d9b674e99e424",
        "repo": "registry.hub.docker.com/minio/mc",
        "tag": "latest"
      },
      "netdata": {
        "amd64_sha256": "95e74c36f15091bcd7983ee162248f1f91c21207c235fce6b0d6f8ed9a11732a",
        "arm64_sha256": "cd3dc9d182a4561b162f03c6986f4647bbb704f8e7e4872ee0611b1b9e86e1b0",
        "repo": "registry.hub.docker.com/netdata/netdata",
        "tag": "latest"
      },
      "vere": {
        "amd64_sha256": "4ff19a35e33a81d1233aef1562b3d5a8f78a9442d9f3d3f28c08c6dd0dc801e7",
        "arm64_sha256": "None",
        "repo": "registry.hub.docker.com/nativeplanet/urbit",
        "tag": "edge"
      },
      "webui": {
        "amd64_sha256": "cc6ea93a53dcd50bef7be7077c41dc475943baee83343cece13884cb2a351308",
        "arm64_sha256": "eebd8b1041fc5216922d36760b884d6ee80cf42a4bf7afe3a3a397411ee2eb4b",
        "repo": "registry.hub.docker.com/nativeplanet/groundseg-webui",
        "tag": "latest"
      },
      "wireguard": {
        "amd64_sha256": "ae6f8e8cc1303bc9c0b5fa1b1ef4176c25a2c082e29bf8b554ce1196731e7db2",
        "arm64_sha256": "403d741b1b5bcf5df1e48eab0af8038355fae3e29419ad5980428f9aebd1576c",
        "repo": "registry.hub.docker.com/linuxserver/wireguard",
        "tag": "latest"
      }
    },
    "edge": {
      "groundseg": {
        "amd64_sha256": "746baf4406aa87b04ffeb3184a72dd1b4f26f90f844b1954e56ea680155df799",
        "amd64_url": "https://files.native.computer/bin/groundseg_amd64_v1.4.3_edge",
        "arm64_sha256": "f84a6cf87981091e0168492dd3717aa61579ecf6ca24c7c6e0d72e7049cadcad",
        "arm64_url": "https://files.native.computer/bin/groundseg_arm64_v1.4.3_edge",
        "major": 1,
        "minor": 4,
        "patch": 3
      },
      "manual": {
        "amd64_sha256": "23ecf8748d797bc6e450aa69523f3ca9377dd0657ea652ad3f1c3521ad65b4cb",
        "arm64_sha256": "006864e0199eae9f773dd93c54bc395ea6eb28f02e43f9105338dda53543b224",
        "repo": "registry.hub.docker.com/nativeplanet/groundseg-manual",
        "tag": "edge"
      },
      "minio": {
        "amd64_sha256": "6d6cf693fd70ca6e15709fa44d39b44f98fc5b58795697486a95ac1cc2ad9880",
        "arm64_sha256": "510eb939d4651d02806e696ff37c71902a17b8297b4a241670f7b59fd2eb4415",
        "repo": "registry.hub.docker.com/minio/minio",
        "tag": "latest"
      },
      "miniomc": {
        "amd64_sha256": "3455a7bae6058ea83f797a95c0e29a4daedff6f79b1f87a0ede429e0344734ab",
        "arm64_sha256": "599ceab1947ab8694e63d7c5e708e616d8dcc77cc26d4e9c36e20100efe84025",
        "repo": "registry.hub.docker.com/minio/mc",
        "tag": "latest"
      },
      "netdata": {
        "amd64_sha256": "95e74c36f15091bcd7983ee162248f1f91c21207c235fce6b0d6f8ed9a11732a",
        "arm64_sha256": "cd3dc9d182a4561b162f03c6986f4647bbb704f8e7e4872ee0611b1b9e86e1b0",
        "repo": "registry.hub.docker.com/netdata/netdata",
        "tag": "latest"
      },
      "vere": {
        "amd64_sha256": "27c6666a504349897d898e13798cb474849105f53f552fd70174a3fbb1570a8b",
        "arm64_sha256": "a19882328811d1716f6747a10e9ff1e542079ca765fbdaa1c7c0d6990f057f11",
        "repo": "registry.hub.docker.com/nativeplanet/urbit",
        "tag": "v2.12"
      },
      "webui": {
        "amd64_sha256": "cc6ea93a53dcd50bef7be7077c41dc475943baee83343cece13884cb2a351308",
        "arm64_sha256": "eebd8b1041fc5216922d36760b884d6ee80cf42a4bf7afe3a3a397411ee2eb4b",
        "repo": "registry.hub.docker.com/nativeplanet/groundseg-webui",
        "tag": "edge"
      },
      "wireguard": {
        "amd64_sha256": "ae6f8e8cc1303bc9c0b5fa1b1ef4176c25a2c082e29bf8b554ce1196731e7db2",
        "arm64_sha256": "403d741b1b5bcf5df1e48eab0af8038355fae3e29419ad5980428f9aebd1576c",
        "repo": "registry.hub.docker.com/linuxserver/wireguard",
        "tag": "latest"
      }
    },
    "latest": {
      "groundseg": {
        "amd64_sha256": "746baf4406aa87b04ffeb3184a72dd1b4f26f90f844b1954e56ea680155df799",
        "amd64_url": "https://files.native.computer/bin/groundseg_amd64_v1.4.3_latest",
        "arm64_sha256": "f84a6cf87981091e0168492dd3717aa61579ecf6ca24c7c6e0d72e7049cadcad",
        "arm64_url": "https://files.native.computer/bin/groundseg_arm64_v1.4.3_latest",
        "major": 1,
        "minor": 4,
        "patch": 3
      },
      "manual": {
        "amd64_sha256": "23ecf8748d797bc6e450aa69523f3ca9377dd0657ea652ad3f1c3521ad65b4cb",
        "arm64_sha256": "006864e0199eae9f773dd93c54bc395ea6eb28f02e43f9105338dda53543b224",
        "repo": "registry.hub.docker.com/nativeplanet/groundseg-manual",
        "tag": "latest"
      },
      "minio": {
        "amd64_sha256": "6d6cf693fd70ca6e15709fa44d39b44f98fc5b58795697486a95ac1cc2ad9880",
        "arm64_sha256": "510eb939d4651d02806e696ff37c71902a17b8297b4a241670f7b59fd2eb4415",
        "repo": "registry.hub.docker.com/minio/minio",
        "tag": "latest"
      },
      "miniomc": {
        "amd64_sha256": "3455a7bae6058ea83f797a95c0e29a4daedff6f79b1f87a0ede429e0344734ab",
        "arm64_sha256": "599ceab1947ab8694e63d7c5e708e616d8dcc77cc26d4e9c36e20100efe84025",
        "repo": "registry.hub.docker.com/minio/mc",
        "tag": "latest"
      },
      "netdata": {
        "amd64_sha256": "95e74c36f15091bcd7983ee162248f1f91c21207c235fce6b0d6f8ed9a11732a",
        "arm64_sha256": "cd3dc9d182a4561b162f03c6986f4647bbb704f8e7e4872ee0611b1b9e86e1b0",
        "repo": "registry.hub.docker.com/netdata/netdata",
        "tag": "latest"
      },
      "vere": {
        "amd64_sha256": "27c6666a504349897d898e13798cb474849105f53f552fd70174a3fbb1570a8b",
        "arm64_sha256": "a19882328811d1716f6747a10e9ff1e542079ca765fbdaa1c7c0d6990f057f11",
        "repo": "registry.hub.docker.com/nativeplanet/urbit",
        "tag": "v2.12"
      },
      "webui": {
        "amd64_sha256": "cc6ea93a53dcd50bef7be7077c41dc475943baee83343cece13884cb2a351308",
        "arm64_sha256": "eebd8b1041fc5216922d36760b884d6ee80cf42a4bf7afe3a3a397411ee2eb4b",
        "repo": "registry.hub.docker.com/nativeplanet/groundseg-webui",
        "tag": "latest"
      },
      "wireguard": {
        "amd64_sha256": "ae6f8e8cc1303bc9c0b5fa1b1ef4176c25a2c082e29bf8b554ce1196731e7db2",
        "arm64_sha256": "403d741b1b5bcf5df1e48eab0af8038355fae3e29419ad5980428f9aebd1576c",
        "repo": "registry.hub.docker.com/linuxserver/wireguard",
        "tag": "latest"
      }
    }
  }
}
```