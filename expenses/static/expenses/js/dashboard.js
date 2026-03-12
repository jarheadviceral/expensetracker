document.addEventListener('DOMContentLoaded', () => {
  const categoryNode = document.getElementById('category-data');
  const monthlyNode = document.getElementById('monthly-data');

  if (!categoryNode || !monthlyNode) return;

  const categoryData = JSON.parse(categoryNode.textContent || '[]');
  const monthlyData = JSON.parse(monthlyNode.textContent || '[]');

  const pieCanvas = document.getElementById('categoryPie');
  if (pieCanvas && categoryData.length) {
    new Chart(pieCanvas, {
      type: 'pie',
      data: {
        labels: categoryData.map(row => row.category),
        datasets: [{
          data: categoryData.map(row => row.total),
          backgroundColor: ['#1dd1a1', '#54a0ff', '#f368e0', '#feca57', '#ff6b6b', '#5f27cd', '#8395a7']
        }]
      }
    });
  }

  const lineCanvas = document.getElementById('monthlyLine');
  if (lineCanvas && monthlyData.length) {
    new Chart(lineCanvas, {
      type: 'line',
      data: {
        labels: monthlyData.map(row => row.month),
        datasets: [{
          label: 'Monthly Spend',
          data: monthlyData.map(row => row.total),
          borderColor: '#76e6ff',
          backgroundColor: 'rgba(118, 230, 255, 0.2)',
          fill: true,
          tension: 0.3
        }]
      },
      options: {
        scales: {
          y: { beginAtZero: true }
        }
      }
    });
  }
});
