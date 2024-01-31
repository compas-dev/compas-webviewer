import axios from "axios";

const HOST = "http://localhost:8000";

export default {
  async ping() {
    let response = await axios.get(HOST + "/ping");
    return response.data;
  },

  async boxToSubdividedMesh(boxdata) {
    let response = await axios.post(HOST + "/box_to_subdivided_mesh", {
      xsize: boxdata.xsize,
      ysize: boxdata.ysize,
      zsize: boxdata.zsize,
    });
    return response.data;
  },
};
