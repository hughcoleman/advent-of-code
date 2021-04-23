// ==UserScript==
// @name         Advent of Code
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  Add navigation buttons to the Advent Of Code pages.
// @author       github.com/hughcoleman/aoc
// @match        https://adventofcode.com/*/day/*
// @icon         https://adventofcode.com/favicon.png
// @grant        none
// @run-at       document-start
// ==/UserScript==

/**
 * This UserScript adds a forum-thread style navigation bar to Advent of Code
 * pages.
 *
 *     < Previous | 17 18 19 [20] 21 22 23 | Next >
 */

(function() {
    'use strict';

    window.addEventListener("load", function() {
        // Determine the year and date of the currently-opened puzzle page.
        let [, year, day] =
            location.href.match(/^https?:\/\/adventofcode\.com\/(\d{4})\/day\/(\d{1,2})$/);
        year = parseInt(year);
        day  = parseInt(day);

        function linkTo(_year, _day, textContent) {
            var el;

            // If the specified _year/_day combination does not exist (on the
            // Calendar), then do not link.
            if (_year < 2015 || _day < 1 || _day > 25) {
                el = document.createElement("span");
            }

            // If the specified puzzle is the current puzzle, then also do not
            // link. However, emphasize it.
            else if (year == _year && day == _day) {
                el = document.createElement("em");
            }

            // Otherwise, determine the time that the specified puzzle unlocks.
            // If it's unlocked, link to it; if it's not, then use a muted,
            // unclickable "link".
            else {
                // Could this be any shittier?
                var ts = new Date(`December ${_day} ${_year} 05:00:00 UTC`);

                if (ts <= (new Date(/* NOW */))) {
                    el = document.createElement("a");
                    el.href = `https://adventofcode.com/${_year}/day/${_day}`;
                } else {
                    el = document.createElement("span");
                    el.classList.add("quiet");
                }

            }

            el.innerText = textContent;
            return el;
        }

        var container = document.createElement("p");
        container.style.textAlign = "right";

        // Create the navigation bar.
        {
            container.appendChild(linkTo(year, day - 1, "< Previous"));
            container.appendChild(document.createTextNode(" | "));
            for (var i = Math.max(1, day - 3); i <= Math.min(day + 3, 25); i++) {
                container.appendChild(linkTo(year, i, i.toString(10)));
                if (i != Math.min(day + 3, 25)) {
                    container.appendChild(document.createTextNode(" "));
                }
            }
            container.appendChild(document.createTextNode(" | "));
            container.appendChild(linkTo(year, day + 1, "Next >"));
        }

        document.querySelector("article.day-desc").insertBefore(
            container, document.querySelector("article.day-desc").firstChild
        );
    });
})();
