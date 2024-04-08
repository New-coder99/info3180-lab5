<template>
  <div>
    <form @submit.prevent="saveMovie">
      <div class="form-group mb-3">
        <label for="title" class="form-label">Movie Title</label>
        <input type="text" v-model="formData.title" name="title" class="form-control" />
      </div>
      <div class="form-group mb-3">
        <label for="director" class="form-label">Director</label>
        <input type="text" v-model="formData.director" name="director" class="form-control" />
      </div>
      <div class="form-group mb-3">
        <label for="year" class="form-label">Release Year</label>
        <input type="number" v-model="formData.year" name="year" class="form-control" />
      </div>
      <div class="form-group mb-3">
        <label for="genre" class="form-label">Genre</label>
        <input type="text" v-model="formData.genre" name="genre" class="form-control" />
      </div>
      <div class="form-group mb-3">
        <button type="submit" class="btn btn-primary">Submit</button>
      </div>
    </form>
  </div>
</template>


<script setup>
  import { ref, onMounted } from 'vue';

  let formData = ref({
    title: '',
    director: '',
    year: null,
    genre: ''
  });

  let csrf_token = ref("");

  function getCsrfToken() {
    fetch('/api/v1/csrf-token')
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        csrf_token.value = data.csrf_token;
      });
  }

  onMounted(() => {
    getCsrfToken();
  });

  function saveMovie() {
    let movieForm = document.getElementById('movieForm');
    let form_data = new FormData(movieForm);
    
    fetch("/api/v1/movies", {
      method: 'POST',
      body: form_data,
      headers: {
        'X-CSRFToken': csrf_token.value
      }
    })
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      // Display a success message
      console.log(data);
    })
    .catch(function (error) {
      console.log(error);
    });
  }
</script>