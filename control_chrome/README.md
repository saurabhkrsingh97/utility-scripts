## control_chrome
![stability-wip](https://img.shields.io/badge/stability-work_in_progress-lightgrey.svg)

This is a rough sample script which can be used to control some actions of Google Chrome as shown below, and can be extended to include almost any functionality available thorugh the [Chrome JavaScript APIs](https://developer.chrome.com/extensions/api_index).

It will require installing [chromix-too](https://www.npmjs.com/package/chromix-too) and running `chromix-too-server` on a separate terminal before using this script.

Also, the [chromix-too Chrome Extension](https://chrome.google.com/webstore/detail/chromix-too/ppapdfccnamacakfkpfmpfnefpeajboj) has to be installed from the Chrome Web Store.

### USAGE:
  `python3 control_chrome.py COMMAND`

`COMMAND`s available:
* `goto URL` - Navigates the tab to `URL` specified
* `previous` - Go back in history
* `forward` - Go forward in history
* `reload` - Reloads current tab
* `close` - Closes current tab
* `pin` - Pins current tab
* `unpin` - Unpins current tab
* `scrollDown N`, `smoothScrollDown N` - Scrolls down by `N` pixels
* `scrollUp N`, `smoothScrollUp N` - Scrolls up by `N` pixels
* `duplicate` - Duplicates current tab
* `bookmark` - Bookmarks current tab
* `openLink N` - Clicks on the `N`th search result link on Google search results page
* `details` - Displays some details about the current tab (tid, title, url)
* `speak` - Speaks the title of the current tab

:octocat:
