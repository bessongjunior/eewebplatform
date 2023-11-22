// /** @type {import('tailwindcss').Config} */
// export default {
//   content: [],
//   theme: {
//     extend: {},
//   },
//   plugins: [],
// }

// https://v2.tailwindcss.com/docs/guides/create-react-app

  // tailwind.config.js
module.exports = {
    // purge: [],
    // purge: ['./src/**/*.{js,jsx,ts,tsx}', './public/index.html'],
    purge: ['./src/**/*.{js,jsx,ts,tsx}'],
     darkMode: false, // or 'media' or 'class'
     theme: {
       extend: {},
     },
     variants: {
       extend: {},
     },
     plugins: [],
}

