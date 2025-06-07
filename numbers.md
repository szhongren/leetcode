# Modern Hardware Performance Benchmarks

## Modern Hardware

- 128GB-512GB RAM is common, 1TB+ in high-performance servers
- Storage: effectively unlimited with cloud solutions
- 10-100Gbps network speeds in data centers
- CPUs: 32-128 cores per machine common in production

## Caching Systems (Redis/Memcached)

- Memory: 32GB-512GB per instance, clusters can reach 10TB+
- Throughput: 500K-2M ops/sec on single node
- Latency: 0.1-1ms
- Network bandwidth: 10-40Gbps

## Databases

### RDBMS (PostgreSQL/MySQL)

- Storage: 1TB-20TB per node
- Reads: 10K-30K QPS (queries per second)
- Writes: 5K-15K TPS (transactions per second)
- Read latency: 5-15ms
- Write latency: 10-30ms
- Concurrent connections: 10K-30K

### NoSQL (MongoDB/Cassandra/DynamoDB)

- Storage: 10TB-50TB per node, easily 100TB+ clusters
- Reads: 50K-200K QPS
- Writes: 10K-80K TPS
- Read latency: 1-10ms
- Write latency: 5-20ms

## Application Servers

- Memory: 8GB-64GB per instance
- Throughput: 10K-100K req/sec
- Latency: 10-100ms for API responses
- Concurrent connections: 20K-100K

## Message Queues (Kafka/RabbitMQ/SQS)

- Throughput: 100K-1M+ msgs/sec per broker
- Latency: 1-5ms publisher to broker, 10-50ms end-to-end
- Storage: 100GB-10TB+ per broker
- Retention: Days to months of data

## Storage Performance

- SSD/NVMe: 400K-1M IOPS
- Read speed: 3-7GB/sec
- Write speed: 2-5GB/sec
