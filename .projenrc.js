const { Project } = require('projen');

const project = new Project({
  /* ProjectOptions */
  // outdir: '.',        /* The root directory of the project. */
  // parent: undefined,  /* The parent project, if this project is part of a bigger project. */
});

project.synth();