It can be detected by storing the previous scrollTop value and comparing the current scrollTop value with it.
JS :
var lastScrollTop = 0;
// element should be replaced with the actual target element on which you have applied scroll, use window in case of no target element.
element.addEventListener("scroll", function(){ // or window.addEventListener("scroll"....
   var st = window.pageYOffset || document.documentElement.scrollTop; // Credits: "https://github.com/qeremy/so/blob/master/so.dom.js#L426"
   if (st > lastScrollTop){
      // downscroll code
   } else {
      // upscroll code
   }
   lastScrollTop = st <= 0 ? 0 : st; // For Mobile or negative scrolling
}, false);
shareimprove this answer
edited Jun 3 '18 at 5:56
Peter Rader
6,48888 gold badges4040 silver badges8686 bronze badges
answered Jul 4 '15 at 18:12
Prateek
2,56211 gold badge1414 silver badges2020 bronze badges
15
It would be safer to initialize lastScrollTop to pageYOffset || scrollTop rather than assuming 0 – Ed Ballot Jul 4 '15 at 18:17
Totally agree !! Thanks @EdBallot. We should initialize the same on window.onload event. – Prateek Jul 4 '15 at 18:34
@Prateek Thanks for your answer but it isn't working for me... I am trying to 'change scene' in my webapp which is built using Tumult Hype. – dwinnbrown Jul 4 '15 at 18:49
I have added few comments in my answer, please check it. I guess you are using "element.addEventListener". – Prateek Jul 4 '15 at 18:59
@Prateek still nothing I'm afraid. Could it be to do with the fact that, I am running it on page load? Here is a screenshot: i.imgur.com/Q0H0T4s.png – dwinnbrown Jul 4 '15 at 19:05 
show 4 more comments
46
Simple way to catch all scroll events (touch and wheel)
window.onscroll = function(e) {
  // print "false" if direction is down and "true" if up
  console.log(this.oldScroll > this.scrollY);
  this.oldScroll = this.scrollY;
}
shareimprove this answer
edited Aug 16 '17 at 17:56
answered Aug 16 '17 at 17:10
IT VLOG
49344 silver badges44 bronze badges
8
Welcome to SO, if you add a desctription to your answer, this can be more helpfull to the OP and to others. – Alejandro Montilla Aug 16 '17 at 17:37
add a comment
26
Use this to find the scroll direction. This is only to find the direction of the Vertical Scroll. Supports all cross browsers.
var scrollableElement = document.body; //document.getElementById('scrollableElement');
scrollableElement.addEventListener('wheel', checkScrollDirection);
function checkScrollDirection(event) {
  if (checkScrollDirectionIsUp(event)) {
    console.log('UP');
  } else {
    console.log('Down');
  }
}
function checkScrollDirectionIsUp(event) {
  if (event.wheelDelta) {
    return event.wheelDelta > 0;
  }
  return event.deltaY < 0;
}
Example
shareimprove this answer
edited Jan 2 at 10:44
Community♦
111 silver badge
answered Jun 15 '17 at 15:59
Vasi
69366 silver badges1616 bronze badges
2
This is good, but only seems to work for using the scroll wheel – Jonathan.Brink Oct 2 '18 at 20:03
add a comment
9
You can try doing this.
function scrollDetect(){
  var lastScroll = 0;
  window.onscroll = function() {
      let currentScroll = document.documentElement.scrollTop || document.body.scrollTop; // Get Current Scroll Value
      if (currentScroll > 0 && lastScroll <= currentScroll){
        lastScroll = currentScroll;
        document.getElementById("scrollLoc").innerHTML = "Scrolling DOWN";
      }else{
        lastScroll = currentScroll;
        document.getElementById("scrollLoc").innerHTML = "Scrolling UP";
      }
  };
}
scrollDetect();
html,body{
  height:100%;
  width:100%;
  margin:0;
  padding:0;
}
.cont{
  height:100%;
  width:100%;
}
.item{
  margin:0;
  padding:0;
  height:100%;
  width:100%;
  background: #ffad33;
}
.red{
  background: red;
}
p{
  position:fixed;
  font-size:25px;
  top:5%;
  left:5%;
}
<div class="cont">
  <div class="item"></div>
  <div class="item red"></div>
  <p id="scrollLoc">0</p>
</div>
 Run code snippetExpand snippet
shareimprove this answer
edited Jun 20 '18 at 8:14
answered Jun 20 '18 at 6:38
davecar21
2,0271313 silver badges2727 bronze badges
this is not working fine for me. When I scroll up even upto some certain height it shows down – Developer Aug 14 '18 at 20:22
add a comment
8
This is an addition to what prateek has answered.There seems to be a glitch in the code in IE so i decided to modify it a bit nothing fancy(just another condition)
$('document').ready(function() {
var lastScrollTop = 0;
$(window).scroll(function(event){
   var st = $(this).scrollTop();
   if (st > lastScrollTop){
       console.log("down")
   }
   else if(st == lastScrollTop)
   {
     //do nothing 
     //In IE this is an important condition because there seems to be some instances where the last scrollTop is equal to the new one
   }
   else {
      console.log("up")
   }
   lastScrollTop = st;
});});
shareimprove this answer
answered Jul 17 '17 at 8:25
Emmanual
9511 silver badge66 bronze badges
1
Thanks for your hint ... this seems to be connected to IE "Smooth Scrolling" option – Kristo Mar 7 '18 at 23:10
add a comment
3
You can get the scrollbar position using document.documentElement.scrollTop. And then it is simply matter of comparing it to the previous position.
shareimprove this answer
answered Jul 4 '15 at 17:31
Igal S.
7,52133 gold badges2323 silver badges3939 bronze badges
Ok and could I still use this on a website which won't traditionally allow scrolling (i.e. it fits the browser 100% width and height. Thanks – dwinnbrown Jul 4 '15 at 17:35
add a comment
3
Initialize an oldValue
Get the newValue by listening to the event
Subtract the two
Conclude from the result
Update oldValue with the newValue
// Initialization
let oldValue = 0;
//Listening on the event
window.addEventListener('scroll', function(e){
    newValue = window.pageYOffset; // Get the new Value
    if(oldValue - newValue < 0) console.log("Up"); //Subtract the two and conclude
    else if(oldValue - newValue > 0) console.log("Down");
    oldValue = newValue; // Update the old value
});

I personally use this code to detect scroll direction in javascript... Just you have to define a variable to store lastscrollvalue and then use this if&else
let lastscrollvalue;
function headeronscroll() {
    // document on which scroll event will occur
    var a = document.querySelector('.refcontainer'); 
    if (lastscrollvalue == undefined) lastscrollvalue = a.scrollTop; // sets lastscrollvalue
    else if (a.scrollTop > lastscrollvalue) lastscrollvalue = a.scrollTop; // downscroll rules will be here
    else if (a.scrollTop < lastscrollvalue) lastscrollvalue = a.scrollTop; // upscroll rules will be here
}
