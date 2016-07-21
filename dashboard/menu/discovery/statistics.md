# Statistics

![Discovery statistics](/img/discovery-statistics.png)

<body>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap-theme.min.css">
    <script src="https://code.jquery.com/jquery-1.11.2.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>
    <script>
        function on100() {
            $(".one").css("background-color", "yellow");
            $(".two").css("background-color", "LightGreen");
            $(".three").css("background-color", "LightBlue");
            $(".four").css("background-color", "LightGrey");
            $(".five").css("background-color", "pink");
        }

        function off100() {
            $(".one").css("background-color", "white");
            $(".two").css("background-color", "white");
            $(".three").css("background-color", "white");
            $(".four").css("background-color", "white");
            $(".five").css("background-color", "white");
        }

        function on99() {
            $(".one99").css("background-color", "yellow");
            $(".two99").css("background-color", "LightGreen");
            $(".three99").css("background-color", "LightBlue");
            $(".four99").css("background-color", "LightGrey");
            $(".five99").css("background-color", "pink");
        }

        function off99() {
            $(".one99").css("background-color", "white");
            $(".two99").css("background-color", "white");
            $(".three99").css("background-color", "white");
            $(".four99").css("background-color", "white");
            $(".five99").css("background-color", "white");
        }

        function on98() {
            $(".one98").css("background-color", "yellow");
            $(".two98").css("background-color", "LightGreen");
            $(".three98").css("background-color", "LightBlue");
            $(".four98").css("background-color", "LightGrey");
            $(".five98").css("background-color", "pink");
        }

        function off98() {
            $(".one98").css("background-color", "white");
            $(".two98").css("background-color", "white");
            $(".three98").css("background-color", "white");
            $(".four98").css("background-color", "white");
            $(".five98").css("background-color", "white");
        }
    </script>
    <style type="text/css">
        .ui-field {
            font-weight: bold;
        }
        
        .ui-value {
            font-style: italic;
        }
        
        .ui-button {
            font-weight: bold;
        }
        
        .pad {
            padding: 3px;
        }
    </style>

    <body class="container">
        <h1 translate="no"><center>Lesson 101 - Understanding Statistics</center></h1>
        <p translate="no">To understand the way statistics work in Easyling, we have to start with the most important fact: in our application, the largest unit of measurement is a <b>block</b>, which is usually represented by a <b>&lt;p&gt;</b> or a <b>&lt;div&gt;</b>. Blocks break down to segments, segments to words, words to letters. Since Easyling deals exclusively with content in webpages, HTML tags also play an important part in weighing the repetitions.</p>
        <p translate="no">It is also important to note that the statistics in Easyling are different degrees of repetitions. The website's content is repetitioned agaist itself, simulating a translation process, not unlike the Homogeneity feature in MemoQ.</p>
        <p translate="no">With that in mind, here is a breakdown of the percentages in our Statistics. You can find these explanations if you hover your mouse over each repetition row:</p>
        <center><img src="/4.png"></center>
        <h3 translate="no">102% - Strong contextual repetitions</h3>
        <p translate="no">These are block repetitions. Every segment in the block is a 101% repetition, and all the tags are identical. We do not charge for these repetitions and they are propagated automatically within the project.</p>
        <h3 translate="no">101% - Contextual repetitions</h3>
        <p translate="no">These repetitions are comparable to the 101% repetitions in MemoQ, or Context Matches in SDL Trados Studio. Both tags in the segment, and contexts (segments immediately before and after) repetition.</p>
        <h3 translate="no">100% - Regular repetitions</h3>
        <p translate="no">This one is straightforward, and comparable to the Repetitions count in MemoQ or Trados. The segment is repeated exactly, including all tags.</p>
        <h3 translate="no">99% - Strong fuzzy repetitions</h3>
        <p translate="no">In this case, a repetition is found after few transformations on the segment before comparing: tags from the ends are stripped out, words lowercased, numbers ignored.</p>
        <h3 translate="no">98% - Weak fuzzy repetitions</h3>
        <p translate="no">Here, all tags are stripped out, not just the ones in the end; words lowercased, numbers ignored.</p>
        <hr>
        <p translate="no">Hover your mouse over the matches to see the differences highlighted.</p>
        <table border="1">
            <thead>
                <tr>
                    <th class="pad" translate="no">Original</th>
                    <th class="pad" translate="no">Repetition</th>
                    <th class="pad" translate="no">Explanation</th>
                </tr>
            </thead>
            <tbody>

                <tr>
                    <td class="pad" onmouseover="$('.102 span').css('background-color', 'yellow')" onmouseout="$('.102 span').css('background-color', 'white')">
                        <div class="102 src"><span>The <b>quick, brown</b> <a href="http://en.wikipedia.org/wiki/Fox">fox</a> jumps over the lazy dog. The dog gets really angry, and chases away the fox. The fox regrets the whole thing and quits jumping, <i>leading</i> to its ultimate demise. The dog lives happily ever after. The End of story 1.</span></div>
                    </td>
                    <td class="pad" onmouseover="$('.102 span').css('background-color', 'yellow')" onmouseout="$('.102 span').css('background-color', 'white')">
                        <div class="102 tar"><span>The <b>quick, brown</b> <a href="http://en.wikipedia.org/wiki/Fox">fox</a> jumps over the lazy dog. The dog gets really angry, and chases away the fox. The fox regrets the whole thing and quits jumping, <i>leading</i> to its ultimate demise. The dog lives happily ever after. The End of story 1.</span></div>
                    </td>
                    <td class="pad" translate="no">102% match. They are completely identical.</td>
                </tr>

                <tr>
                    <td class="pad" onmouseover="$('.101').css('background-color', 'yellow'); $('.not101').css('background-color', 'LightGreen');" onmouseout="$('.101').css('background-color', 'white'); $('.not101').css('background-color', 'white');">
                        <div class="src"><span class="101">The <b>quick, brown</b> <a href="http://en.wikipedia.org/wiki/Fox">fox</a> jumps over the lazy dog. The dog gets really angry, and chases away the fox. The fox regrets the whole thing and quits jumping, <i>leading</i> to its ultimate demise. The dog lives happily ever after. The End of story 1.</span></div>
                    </td>
                    <td class="pad" onmouseover="$('.101').css('background-color', 'yellow'); $('.not101').css('background-color', 'LightGreen');" onmouseout="$('.101').css('background-color', 'white'); $('.not101').css('background-color', 'white');">
                        <div class="tar"><span class="101">The <b>quick, brown</b> <a href="http://en.wikipedia.org/wiki/Fox">fox</a> jumps over the lazy dog. The dog gets really angry, and chases away the fox. The fox regrets the whole thing and quits jumping, <i>leading</i> to its ultimate demise. The dog lives happily ever after. The End of story 1.</span> <span class="not101">Not!</span></div>
                    </td>
                    <td class="pad" translate="no">101%, 5 repetitions. By adding another segment to the block, the first 5 sentences become 101% repetitions, but the last one is unique, therefore it is not a 102% match.</td>
                </tr>

                <tr>
                    <td class="pad" onmouseover="on100();" onmouseout="off100();"><span class="one">The <b>quick, brown</b> <a href="http://en.wikipedia.org/wiki/Fox">fox</a> jumps over the lazy doge.</span> <span class="two">The doge gets really angry, and chases away the fox.</span> <span class="three">The foxe regrets the whole thing and quits jumping, <i>leading</i> to its ultimate demise.</span> <span class="four">The doge lives happily ever after.</span> <span class="five">The End of story 2.</span></td>
                    <td class="pad" onmouseover="on100();" onmouseout="off100();"><span class="five">The End of story 2.</span> <span class="four">The doge lives happily ever after.</span> <span class="three">The foxe regrets the whole thing and quits jumping, <i>leading</i> to its ultimate demise.</span> <span class="two">The doge gets really angry, and chases away the fox.</span> <span class="one">The <b>quick, brown</b> <a href="http://en.wikipedia.org/wiki/Fox">fox</a> jumps over the lazy doge.</span></td>
                    <td class="pad" translate="no">100%, 5 repetitions. The contents are the same, but the order is reversed, thefore they are not 101 matches anymore.</td>
                </tr>

                <tr>
                    <td class="pad" onmouseover="on99();" onmouseout="off99();"><span class="one99">The <b>quick, brown</b> <a href="http://en.wikipedia.org/wiki/Fox">fox</a> jumps over the lazy doge.</span> <span class="two99">The doge gets really angry, and chases away the fox.</span> <span class="three99">The foxe regrets the whole thing and quits jumping, <i>leading</i> to its ultimate demise.</span> <span class="four99">The doge lives happily ever after.</span> <span class="five99">The End of story 3.</span></td>
                    <td class="pad" onmouseover="on99();" onmouseout="off99();"><span class="five99">The End of story 4.</span> <span class="four99">The DOGE lives happily ever after.</span> <span class="three99">The foxe regrets the whole thing and quits jumping, <i>leading</i> to its ultimate demise.&lt;br/&gt;<br/></span> <span class="two99">The doge gets really angry, and chases away the FOX.</span> <span class="one99">The <b>quick, brown</b> <a href="http://en.wikipedia.org/wiki/Fox">fox</a> JUMPS over the lazy doge.</span></td>
                    <td class="pad" translate="no">99%, 5 repetitions. Aside from the reversed order, some words are in a different case, and one segment even has a tag at the end (&lt;br/&gt;) which is not found in the source.</td>
                </tr>


                <tr>
                    <td class="pad" onmouseover="on98();" onmouseout="off98();"><span class="one98">The <b>quick, brown</b> <a href="http://en.wikipedia.org/wiki/Fox">fox</a> jumps over the lazy doge.</span> <span class="two98">The doge gets really angry, and chases away the fox.</span> <span class="three98">The foxe regrets the whole thing and quits jumping, <i>leading</i> to its ultimate demise.</span> <span class="four98">The doge lives happily ever after.</span> <span class="five98">The End of story 3.</span></td>
                    <td class="pad" onmouseover="on98();" onmouseout="off98();"><span class="five98">The <u>End</u> Of Story 4.</span> <span class="four98">The DOGE lives <u>happily</u> ever after.</span> <span class="three98">The foxe regrets the whole thing and quits jumping, <b>leading</b> to its ultimate demise.&lt;br/&gt;<br/></span> <span class="two98">The doge gets <b>Really Angry</b>, and chases away the FOX.</span> <span class="one98">The <i>quick, brown</i> <a href="http://en.wikipedia.org/wiki/Fox">fox</a> JUMPS over the lazy doge.</span></td>
                    <td class="pad" translate="no">98%, 5 repetitions. Many tags are changed and/or inserted, and more words are in different cases now.</td>
                </tr>

            </tbody>
        </table>
        <br/><br/>
    </body>
