// import { createStore } from "vuex";

// const store = createStore({
//   state: {},
//   mutations: {},
//   actions: {},
//   getters: {},
// });

// export default store;

import { createStore } from "vuex";

import geometry from "./modules/geometry";

const store = createStore({
  modules: {
    geometry,
  },
});

export default store;
