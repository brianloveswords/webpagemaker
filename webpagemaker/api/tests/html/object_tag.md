We want to allow object tags (with param and embed) so users can include
videos. Testing with a user-provided embed and an old-style embed from
YouTube.

```html
<!DOCTYPE html><html><head></head><body>
<object height="220" width="365">
<param name="flashvars" value="config=https://www.radiowaves.co.uk/config_video_21758_1_395461_8_0_0">
<param name="movie" value="https://www.radiowaves.co.uk/FW/CM/SWF/player.swf">
<param name="allowfullscreen">
<embed allowfullscreen="true" flashvars="config=https://www.radiowaves.co.uk/config_video_21758_1_395461_8_0_0" height="220" src="https://www.radiowaves.co.uk/FW/CM/SWF/player.swf" type="application/x-shockwave-flash" width="365">
</object>

<object height="315" width="420"><param name="movie" value="http://www.youtube.com/v/8KswnjMa-MQ?version=3"><param name="allowFullScreen" value="true"><param name="allowscriptaccess" value="always"><embed allowfullscreen="true" allowscriptaccess="always" height="315" src="http://www.youtube.com/v/8KswnjMa-MQ?version=3&amp;hl=en_US" type="application/x-shockwave-flash" width="420"></object>
</body></html>
```
