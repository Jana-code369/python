const ctx = document.getElementById('chart');

new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Chest', 'Back', 'Legs', 'Shoulders', 'Arms'],
        datasets: [{
            label: 'Workout Frequency',
            data: [5, 3, 2, 4, 3]
        }]
    }
});