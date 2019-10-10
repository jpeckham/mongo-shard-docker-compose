Mongo Sharded Cluster with Docker Compose
=========================================
A simple sharded Mongo Cluster with a replication factor of 2 running in `docker` using `docker-compose`.

Designed to be quick and simple to get a local or test environment up and running. Needless to say... DON'T USE THIS IN PRODUCTION!

Heavily inspired by [https://github.com/jfollenfant/mongodb-sharding-docker-compose](https://github.com/jfollenfant/mongodb-sharding-docker-compose)

### Mongo Components

* Config Server (3 member replica set): `config01`,`config02`,`config03`
* 2 Shards (each a 3 member replica set):
	* `shard01a`,`shard01b`,`shard01c`
	* `shard02a`,`shard02b`,`shard02c`
* 1 Router (mongos): `router`
* 1 mongo express `mongo-express` to access data

### First Run (initial setup)
**Start all of the containers** (daemonized)

```
docker-compose up -d
```

**Initialize the replica sets (config server and shards) and router**

```
init.bat
```

This script has a `sleep 20` to wait for the config server and shards to elect their primaries before initializing the router
*todo: set as voting/priority 0 then enable them after secondary per documentation

**Verify the status of the sharded cluster**

```
docker-compose exec router mongo
mongos> sh.status()

```

### Normal Startup
The cluster only has to be initialized on the first run. Subsequent startup can be achieved simply with `docker-compose up` or `docker-compose up -d`

### Accessing the Mongo Shell
Its as simple as:

```
docker-compose exec router mongo
```

### Resetting the Cluster
To remove all data and re-initialize the cluster, make sure the containers are stopped and then:

```
docker-compose rm
```

Execute the **First Run** instructions again.