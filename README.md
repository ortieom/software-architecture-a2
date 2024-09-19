Project structure:

```plaintext
.
├── code  # code for client and server
│   ├── server/  # all code related to server
│   ├── client.py  # client code
│   ├── docker-compose.yaml  # docker compose for launching server
├── tests/  # automated fitness functions
│   ├── # TODO
└── README.md
```

To run server:
```bash
cd code
sudo docker compose up -d
```

To run client:
```bash
cd code
python3 client.py
```
