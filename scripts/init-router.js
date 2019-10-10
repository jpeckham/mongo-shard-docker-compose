sh.addShard("shard01/shard01a:27018")
sh.addShard("shard01/shard01b:27018")
sh.addShard("shard01/shard01c:27018")

sh.addShard("shard02/shard02a:27019")
sh.addShard("shard02/shard02b:27019")
sh.addShard("shard02/shard02c:27019")

sh.enableSharding("mydatabase")
use mydatabase
var shardKey = { "_id": "hashed" }
db.customers.createIndex(shardKey)
sh.shardCollection( "mydatabase.customers", shardKey)