function load_post(post_element, text, username, timePosted) {
    console.log(post_element)
    console.log(text)
    const iframe = post_element.contentDocument.body;
    console.log(iframe);
    const htmlStr = iframe.innerHTML
    .replace("HOOK_POST_TEXT", text.replace("\n","<br>"))
    .replace("HOOK_POST_USERNAME", decodeURI(username) + " @ " + decodeURI(timePosted))
    .replace("HOOK_USERNAME_LINK", "/users/" + username)
    .replace("p class=\"gwd-p-p2ca\"", "a class=\"gwd-p-p2ca\"");
    iframe.innerHTML = htmlStr;
    console.log(htmlStr);
    console.log(iframe.innerHTML);
}