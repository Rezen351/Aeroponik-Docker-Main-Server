# Aeroponik Docker Main Server

This project sets up a comprehensive Docker-based environment for an Aeroponik system using Supabase as the backend. It includes all necessary services for a full-stack application with authentication, database, real-time features, storage, and more.

## Project Structure

- `supabase/` - Supabase source code and configurations
- `supabase-project/` - Docker Compose setup for Supabase services
- `.gitignore` - Git ignore rules for the project

## Prerequisites

- Docker and Docker Compose installed
- Node.js (for development)
- Git

## Quick Start

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Aeroponik-Docker-Main-Server
   ```

2. Copy environment variables:
   ```bash
   cp supabase-project/.env.example supabase-project/.env
   ```

3. Edit the `.env` file with your configuration values.

4. Start the services:
   ```bash
   cd supabase-project
   docker compose up -d
   ```

5. Access the services:
   - Supabase Studio: http://localhost:3000
   - API Gateway: http://localhost:8000
   - Database: localhost:5432

## Services Included

- **Supabase Studio**: Web-based dashboard for managing your Supabase project
- **Kong**: API Gateway and microservices management
- **Auth**: Authentication service
- **REST API**: PostgREST API for database access
- **Realtime**: Real-time subscriptions and broadcasts
- **Storage**: File storage with image transformation
- **Edge Functions**: Serverless functions
- **Analytics**: Logging and analytics
- **Database**: PostgreSQL database
- **Vector**: Log aggregation
- **Pooler**: Connection pooling
- **Mosquitto**: MQTT broker
- **Grafana**: Monitoring and visualization

## Environment Variables

Key environment variables to configure:

- `POSTGRES_PASSWORD`: Database password
- `JWT_SECRET`: JWT signing secret
- `ANON_KEY`: Anonymous API key
- `SERVICE_ROLE_KEY`: Service role API key
- `SUPABASE_PUBLIC_URL`: Public URL for Supabase
- `SITE_URL`: Site URL for authentication

See `supabase-project/.env.example` for a complete list.

## Development

### Starting Development Environment

```bash
cd supabase-project
docker compose -f docker-compose.yml -f ./dev/docker-compose.dev.yml up
```

### Stopping Services

```bash
docker compose down
```

### Reset Everything

```bash
./reset.sh
```

## API Usage

Once running, you can interact with the Supabase API:

- REST API: `http://localhost:8000/rest/v1/`
- GraphQL: `http://localhost:8000/graphql/v1`
- Realtime: `ws://localhost:8000/realtime/v1`

## Database

The PostgreSQL database is available at:
- Host: localhost
- Port: 5432
- Database: postgres
- User: postgres

## Monitoring

- Grafana: http://localhost:3010 (default password: admin)

## MQTT

Mosquitto MQTT broker is available at:
- TCP: localhost:1883
- WebSocket: localhost:9001

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## Troubleshooting

### Common Issues

1. **Port conflicts**: Ensure the required ports are available
2. **Environment variables**: Double-check your `.env` file
3. **Disk space**: Docker volumes can consume significant space

### Logs

View logs for specific services:
```bash
docker compose logs <service-name>
```

### Reset Database

To completely reset the database:
```bash
docker compose down -v
docker compose up -d
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues and questions:
- Check the [Supabase Documentation](https://supabase.com/docs)
- Open an issue in this repository
