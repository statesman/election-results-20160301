var fs = require("fs");

module.exports = function(grunt) {
  'use strict';

  // Project configuration.
  grunt.initConfig({

    // Copy FontAwesome files to the fonts/ directory
    copy: {
      fonts: {
        src: 'bower_components/font-awesome/fonts/**',
        dest: 'public/fonts/',
        flatten: true,
        expand: true
      }
    },

    // Transpile LESS

/*     less: {
      options: {
        paths: ['bower_components/bootstrap/less']
      },
      prod: {
        options: {
          compress: true,
          cleancss: true
        },
        files: {
          "public/dist/style.css": "src/css/style.less"
        }
      }
    },
*/
    // Transpile LESS
   less: {
      options: {
        sourceMap: true,
        paths: ['bower_components/bootstrap/less']
      },
      prod: {
        options: {
          compress: true,
          cleancss: false
        },
        files: {
          "public/dist/style.css": "src/less/style.less"
        }
      }
    },


    // Pre-render Handlebars templates
    handlebars: {
      options: {
        // Returns the filename, with its parent directory if
        // it's in a subdirectory of the src/templates folder
        processName: function(filePath) {
          var path = filePath.toLowerCase(),
              pieces = path.split("/"),
              name = '';
          if(pieces[pieces.length - 2] !== 'templates') {
            name = name + pieces[pieces.length - 2];
          }
          name = name + pieces[pieces.length - 1];
          return name.split(".")[0];
        }
      },
      compile: {
        files: {
          'build/templates.js': ['src/templates/**.hbs']
        }
      }
    },

    // Run our JavaScript through JSHint
    jshint: {
      js: {
        src: ['src/js/**.js']
      }
    },

    // Use Uglify to bundle up a pym file for the home page
    uglify: {
      options: {
        sourceMap: true
      },
      homepage: {
        files: {
          'public/dist/scripts.js': [
            'bower_components/jquery/dist/jquery.js',
            'bower_components/geocomplete/jquery.geocomplete.js',
            'bower_components/gmaps/gmaps.js',
            'bower_components/underscore/underscore.js',
            'bower_components/handlebars/handlebars.runtime.js',
            'bower_components/numeral/numeral.js',
            'build/templates.js',
            'src/js/palette.js',
            'src/js/key.js',
            'src/js/results.js',
            'src/js/map.js',
            'src/js/main.js'
          ]
        }
      }
    },

// jquery, button, collapse, transition, dropdown

    // Lint our Bootstrap usage
    bootlint: {
      options: {
        relaxerror: ['W005']
      },
      files: 'public/**.php',
    },

    // Watch for changes in LESS and JavaScript files,
    // relint/retranspile when a file changes
    watch: {
      options: {
        livereload: true
      },
      markup: {
        files: ['public/*.php','public/includes/*.inc']
      },
      scripts: {
        files: ['src/js/*.js'],
        tasks: ['jshint', 'uglify']
      },
      styles: {
        files: ['src/less/**/*.less'],
        tasks: ['less']
      }
    },
    // stage path needs to be set
    ftpush: {
      stage: {
        auth: {
          host: 'host.coxmediagroup.com',
          port: 21,
          authKey: 'cmg'
        },
        src: 'public',
        dest: '/stage_aas/projects/databases/election-map-20151103/',
        exclusions: ['dist/tmp','Thumbs.db','.DS_Store'],
        simple: false,
        useList: false
      },
      // prod path will need to change
      prod: {
        auth: {
          host: 'host.coxmediagroup.com',
          port: 21,
          authKey: 'cmg'
        },
        src: 'public',
        dest: '/prod_aas/projects/databases/election-map-20151103/',
        exclusions: ['dist/tmp','Thumbs.db','.DS_Store'],
        simple: false,
        useList: false
      }
    },

    // be sure to set publishing paths
    slack: {
        options: {
          endpoint: fs.readFileSync('.slack', {encoding: 'utf8'}),
          channel: '#bakery',
          username: 'gruntbot',
          icon_url: 'http://vermilion1.github.io/presentations/grunt/images/grunt-logo.png'
        },
        stage: {
          text: 'Project published to stage: http://stage.host.coxmediagroup.com/aas/projects/databases/election-map-20151103/ {{message}}'
        },
        prod: {
          text: 'Project published to prod: http://projects.statesman.com/ {{message}}'
        }
    }


  });

  // Load the task plugins
  grunt.loadNpmTasks('grunt-contrib-less');
  grunt.loadNpmTasks('grunt-contrib-copy');
  grunt.loadNpmTasks('grunt-contrib-jshint');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-contrib-handlebars');
  grunt.loadNpmTasks('grunt-bootlint');
  grunt.loadNpmTasks('grunt-ftpush');
  grunt.loadNpmTasks('grunt-slack-hook');


  grunt.registerTask('default', ['copy', 'less', 'jshint','bootlint','uglify']);
  grunt.registerTask('stage', ['default','ftpush:stage','slack:stage']);
  grunt.registerTask('prod', ['default','ftpush:prod','slack:prod']);

};
