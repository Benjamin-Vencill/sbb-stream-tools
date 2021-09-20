# Stream Tools for Storybook Brawl

## 1. Finish Tracker
To use the finish tracker, run `scripts/form.py`. Enter your results in the form provided. In the streaming software, display the resulting `StreamAssets/Finishes/FrameCollection.png` directly to the screen.

When using OBS, to ensure the image updates, include it as a browser source. To do so, add a new browser souce and select "Local File". Under Custom CSS, replace the default with
```
body { background-color: rgba(0,0,0,0)!important }
```
