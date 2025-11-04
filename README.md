# Aeroponik Full-Stack Application

This project sets up a comprehensive full-stack application for an Aeroponik system using Next.js (TypeScript) as the frontend and Supabase as the backend in a Docker-based environment. It includes all necessary services for authentication, database, real-time features, storage, and more.

## Project Structure

- `frontend/` - Next.js (TypeScript) frontend application
- `supabase/` - Supabase source code and configurations
- `supabase-project/` - Docker Compose setup for Supabase services
- `.gitignore` - Git ignore rules for the project

## Prerequisites

- Docker and Docker Compose installed
- Node.js (version 18 or higher, for frontend development)
- TypeScript (for frontend)
- Git

## Quick Start

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Aeroponik-Docker-Main-Server
   ```

2. Set up the backend (Supabase):
   ```bash
   cd supabase-project
   cp .env.example .env
   # Edit .env with your configuration values
   docker compose up -d
   ```

3. Set up the frontend (Next.js):
   ```bash
   cd ../frontend
   npm install
   npm run dev
   ```

4. Access the applications:
   - Frontend: http://localhost:3000
   - Supabase Studio: http://localhost:3001
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

1. Backend (Supabase):
   ```bash
   cd supabase-project
   docker compose -f docker-compose.yml -f ./dev/docker-compose.dev.yml up
   ```

2. Frontend (Next.js):
   ```bash
   cd frontend
   npm run dev
   ```

### Stopping Services

```bash
# Backend
cd supabase-project
docker compose down

# Frontend (if running separately)
cd frontend
npm run stop
```

### Reset Everything

```bash
cd supabase-project
./reset.sh
```

## API Usage

The Next.js frontend interacts with the Supabase backend via the Supabase JavaScript client. You can also directly interact with the Supabase API:

- REST API: `http://localhost:8000/rest/v1/`
- GraphQL: `http://localhost:8000/graphql/v1`
- Realtime: `ws://localhost:8000/realtime/v1`

### Frontend Integration

In the Next.js app, use the Supabase client:

```typescript
import { createClient } from '@supabase/supabase-js'

const supabase = createClient(
  process.env.NEXT_PUBLIC_SUPABASE_URL!,
  process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!
)
```

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
3. Make your changes (ensure TypeScript types are correct in frontend)
4. Test both frontend and backend thoroughly
5. Submit a pull request

## Troubleshooting

### Common Issues

1. **Port conflicts**: Ensure ports 3000 (frontend), 3001 (Supabase Studio), 8000 (API), etc., are available
2. **Environment variables**: Double-check your `.env` files in both `supabase-project` and `frontend`
3. **Node.js version**: Ensure Node.js 18+ is installed for Next.js
4. **TypeScript errors**: Run `npm run type-check` in frontend to verify types
5. **Disk space**: Docker volumes can consume significant space

### Logs

View logs for specific services:
```bash
# Backend services
cd supabase-project
docker compose logs <service-name>

# Frontend logs (if using a process manager)
cd frontend
npm run logs
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
- Check the [Next.js Documentation](https://nextjs.org/docs) for frontend issues
- Check the [Supabase Documentation](https://supabase.com/docs) for backend issues
- Open an issue in this repository
