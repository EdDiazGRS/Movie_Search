import requests
from datetime import datetime
from rest_framework import viewsets
from rest_framework.response import Response
from django.db.models import Q
from .models import Movie
from .serializers import MovieSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
    def get_queryset(self):
        queryset = Movie.objects.all()
        search_term = self.request.query_params.get('search', None)
        
        if search_term:
            queryset = queryset.filter(title__icontains=search_term)
            
        return queryset
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        search_term = request.query_params.get('search', None)
        
        # If search is provided and no local results found, try external API
        if search_term and not queryset.exists():
            api_key = "Your Key Here"
            tmdb_url = "https://api.themoviedb.org/3/search/movie"
            
            genre_map = {
                28: "Action",
                12: "Adventure",
                16: "Animation",
                35: "Comedy",
                80: "Crime",
                99: "Documentary",
                18: "Drama",
                10751: "Family",
                14: "Fantasy",
                36: "History",
                27: "Horror",
                10402: "Music",
                9648: "Mystery",
                10749: "Romance",
                878: "Science Fiction",
                10770: "TV Movie",
                53: "Thriller",
                10752: "War",
                37: "Western"
        }
            params = {
                'api_key': api_key,
                'query': search_term,
                'language': 'en-US',
                'page': 1
            }
            
            response = requests.get(tmdb_url, params=params)
            print(f"API Status Code: {response.status_code}")  # Debug print
            
            if response.status_code == 200:
                data = response.json()
                print(f"Found {len(data.get('results', []))} results")  # Debug print
                
                for movie_data in data.get('results', [])[:5]:  # Limit to 5 movies
                    # Convert TMDB data to our model format
                    release_date = None
                    if movie_data.get('release_date'):
                        try:
                            release_date = datetime.strptime(movie_data['release_date'], '%Y-%m-%d').date()
                        except ValueError:
                            pass
                    
                      # Map genre IDs to genre names
                    genre_names = []
                    for genre_id in movie_data.get('genre_ids', []):
                        if genre_id in genre_map:
                            genre_names.append(genre_map[genre_id])
                    
                    genre = ", ".join(genre_names) if genre_names else "Unknown"
                    
                    # Create movie in our database
                    Movie.objects.create(
                        title=movie_data.get('title', ''),
                        genre=genre,
                        user_score=int(movie_data.get('vote_average', 0) * 10),  # Convert 0-10 to 0-100
                        release_date=release_date,
                        overview=movie_data.get('overview', '')
                    )
                
                # Query again to get the newly created movies
                queryset = self.get_queryset()
                print(f"After API fetch, now have {queryset.count()} movies")  # Debug print
        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
