<template>
  <div class="movies-container">
    <div v-for="movie in movies" :key="movie.id" class="movie-card">
      <img :src="movie.poster" alt="Movie Poster" class="movie-poster" />
      <div class="movie-details">
        <h2 class="movie-title">{{ movie.title }}</h2>
        <p class="movie-description">{{ movie.description }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";

let movies = ref([]);

function fetchMovies() {
  fetch("/api/v1/movies")
    .then((response) => response.json())
    .then((data) => {
      movies.value = data.movies;
    })
    .catch((error) => {
      console.error("Error fetching movies:", error);
    });
}

onMounted(() => {
  fetchMovies();
});
</script>

<style scoped>
.movies-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-evenly;
}

.movie-card {
  width: 300px;
  margin-bottom: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  overflow: hidden;
}

.movie-poster {
  width: 100%;
  height: auto;
}

.movie-details {
  padding: 10px;
}

.movie-title {
  margin-top: 0;
}

.movie-description {
  margin-bottom: 0;
}
</style>