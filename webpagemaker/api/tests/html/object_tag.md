We want to allow object tags (with param and embed) so users can include videos.

```html
<!DOCTYPE html><html><head></head><body>
<object height="220" width="365">
<param name="flashvars" value="config=https://www.radiowaves.co.uk/config_video_21758_1_395461_8_0_0">
<param name="movie" value="https://www.radiowaves.co.uk/FW/CM/SWF/player.swf">
<param name="allowfullscreen">
<embed allowfullscreen="true" flashvars="config=https://www.radiowaves.co.uk/config_video_21758_1_395461_8_0_0" height="220" src="https://www.radiowaves.co.uk/FW/CM/SWF/player.swf" type="application/x-shockwave-flash" width="365">
</object>
</body></html>
```
