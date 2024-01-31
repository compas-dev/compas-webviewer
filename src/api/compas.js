import axios from "axios";

const HOST = "http://127.0.0.1:8000/";

export default {
  async fetchKeywords() {
    let response = await axios.get(HOST + "api/brg/meta/keyword/");
    return response.data;
  },
};
