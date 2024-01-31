<template>
  <v-container class="pa-0 ma-0">
    <v-row no-gutters>
      <v-col cols="12" class="pa-0 ma-0">
        <v-sheet
          class="bg-blue-grey-lighten-4"
          :height="contentHeight"
          v-resize="onResize"
        >
          <div id="three-container"></div>
        </v-sheet>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import * as THREE from "three";
import { OrbitControls } from "three/addons/controls/OrbitControls.js";

const scene = new THREE.Scene();
scene.background = new THREE.Color(0xeeeeee);

export default {
  data: () => ({
    removeFromTop: 64,
    contentHeight: window.innerHeight - 64,
    config: {
      camera: {
        fov: 75,
        aspect: window.innerWidth / window.innerHeight,
        near: 0.1,
        far: 1000,
      },
      grid: {
        size: 20,
        divisions: 20,
        colorCenterLine: 0x7f7f7f,
        colorGrid: 0xbfbfbf,
      },
    },
  }),

  methods: {
    onResize() {
      this.contentHeight = window.innerHeight - this.removeFromTop;
    },

    initThree() {
      const camera = new THREE.PerspectiveCamera(
        this.config.camera.fov,
        this.config.camera.aspect,
        this.config.camera.near,
        this.config.camera.far
      );
      camera.up.set(0, 0, 1);
      camera.position.set(0, -7, 7);
      camera.lookAt(0, 0, 0);

      const renderer = new THREE.WebGLRenderer({
        antialias: true,
        autoSize: true,
      });
      renderer.setSize(window.innerWidth, this.contentHeight);
      renderer.setAnimationLoop(() => {
        renderer.render(scene, camera);
      });

      document
        .getElementById("three-container")
        .appendChild(renderer.domElement);

      const controls = new OrbitControls(camera, renderer.domElement);
    },

    addBox() {
      const geometry = new THREE.BoxGeometry(1, 1, 1);
      const material = new THREE.MeshBasicMaterial({ color: 0xcccccc });
      const cube = new THREE.Mesh(geometry, material);
      const edges = new THREE.EdgesGeometry(geometry);
      const line = new THREE.LineSegments(
        edges,
        new THREE.LineBasicMaterial({ color: 0xaaaaaa })
      );
      scene.add(cube);
      scene.add(line);
    },

    addAxes() {
      const axes = new THREE.AxesHelper(1);
      scene.add(axes);
    },

    addGrid() {
      const grid = new THREE.GridHelper(
        this.config.grid.size,
        this.config.grid.divisions,
        this.config.grid.colorCenterLine,
        this.config.grid.colorGrid
      );
      grid.rotation.x = Math.PI / 2;
      scene.add(grid);
    },

    setSceneBackground(color) {
      scene.background = new THREE.Color(color);
    },
  },

  mounted() {
    this.initThree();
    this.addGrid();
    this.addAxes();
    this.addBox();
  },
};
</script>
