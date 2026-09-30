# Posting a Kettlon story from Comet (tested 30 Sep 2026)

Instagram desktop web has no story composer. Mobile web does. Recipe that worked, in the browser harness (`browser_exec`, local Comet transport, account @kettlongear already logged in):

1. `start_browser("local")`, then `create_tab("https://www.instagram.com/")`.
2. Emulate an iPhone on that tab:
   `cdp("Emulation.setUserAgentOverride", {"userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/604.1", "platform": "iPhone"})`
   `cdp("Emulation.setDeviceMetricsOverride", {"width": 390, "height": 844, "deviceScaleFactor": 3, "mobile": True, "screenWidth": 390, "screenHeight": 844, "screenOrientation": {"type": "portraitPrimary", "angle": 0}})`
   `cdp("Emulation.setTouchEmulationEnabled", {"enabled": True})`, then `goto_url("https://www.instagram.com/")`. Dismiss "Save your login info?" with Not now if it appears.
3. Comet cannot read sandbox files, so build the File in page from base64: read the story JPEG, base64 it, and inject:
   - `js("(()=>{HTMLInputElement.prototype.click=function(){window.__armed=this;}; return 1})()")` so the native picker never opens.
   - Click the plus icon top right (`click_at_xy(321, 21)`), then the Story menu item (`click_at_xy(304, 101)`). The page navigates to /create/story/ and arms the file input.
   - `js` : atob(base64) to Uint8Array to `new File([...], 'story.jpg', {type:'image/jpeg'})`, DataTransfer, `window.__armed.files = dt.files`, dispatch `change` with bubbles.
4. The page shows "Rotate your device to add to your story." Fix it with
   `js("(()=>{Object.defineProperty(window,'outerWidth',{get:()=>390,configurable:true});Object.defineProperty(window,'outerHeight',{get:()=>844,configurable:true});Object.defineProperty(window,'orientation',{get:()=>0,configurable:true});window.dispatchEvent(new Event('resize'));window.dispatchEvent(new Event('orientationchange'));return 1})()")`
   The buttons Close, Add AI label, Add to your story appear.
5. Click the button whose name contains "Add to your story" via `click_by_ref`. Wait about 20 seconds for "Uploading…" to finish.
6. Verify on https://www.instagram.com/kettlongear/ (the story ring appears around the avatar). Clear emulation (`Emulation.clearDeviceMetricsOverride`), `close_tab(current_tab())`, `stop_browser()`.

Feed posts still go through the desktop composer: New post, click the "Post" tile, inject into the `input[type=file]` whose accept includes video, Next, Next, caption, Share.

If the local browser is unavailable (Comet closed), do not fall back to a cloud browser (no login). Attach the day's story JPEG and caption in the thread and ask Ken to post it from his phone.
