/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        arimo: ['"Arimo"', 'sans-serif'],
      },
      boxShadow: {
        'custom': '0 0 10px rgba(0, 0, 0, .1)'
      },
      colors: {
        'custom-blue': 'rgba(72, 97, 220, 1)',
        'custom-purple': 'rgba(156,126,238,1)'
      }
    },
  },
  plugins: [],
}