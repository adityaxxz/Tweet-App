# TweetApp - Django Social Media App

A simple Twitter-like application built with Django.

## Deployment to Vercel

### Prerequisites

- A Vercel account
- Git installed on your machine
- Python 3.9+ installed

### Local Development Setup

1. Clone the repository
   ```
   git clone <your-repository-url>
   cd tweetapp
   ```

2. Create a virtual environment
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file based on `.env.example`
   ```
   cp .env.example .env
   ```
   Then edit the `.env` file with your settings.

5. Run migrations
   ```
   python manage.py migrate
   ```

6. Run the development server
   ```
   python manage.py runserver
   ```

### Deploying to Vercel

1. Install Vercel CLI
   ```
   npm install -g vercel
   ```

2. Login to Vercel
   ```
   vercel login
   ```

3. Deploy the app
   ```
   vercel
   ```

4. For production deployment
   ```
   vercel --prod
   ```

### Environment Variables

Set these environment variables in your Vercel project settings:

- `SECRET_KEY`: Your Django secret key
- `DEBUG`: Set to 'False' for production
- `DATABASE_URL`: Your PostgreSQL connection string
- `VERCEL_URL`: Your app's Vercel URL (automatically set by Vercel)

### Database Setup

For production, you'll need to set up a PostgreSQL database. You can use:

- Vercel Postgres
- Supabase
- Neon
- Any other PostgreSQL provider

Update the `DATABASE_URL` environment variable with your database connection string.

## Features

- User authentication (login, register, logout)
- Create, read, update, and delete tweets
- Upload images with tweets
- Search functionality for tweets 