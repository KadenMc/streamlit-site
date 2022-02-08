import streamlit as st
st.markdown("""
<style>
/*
The MIT License (MIT)

Copyright (c) 2016 GitHub, Inc.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

*/

.pl-c /* comment */ {
  color: #969896;
}

.pl-c1 /* constant, variable.other.constant, support, meta.property-name, support.constant, support.variable, meta.module-reference, markup.raw, meta.diff.header */,
.pl-s .pl-v /* string variable */ {
  color: #0086b3;
}

.pl-e /* entity */,
.pl-en /* entity.name */ {
  color: #795da3;
}

.pl-smi /* variable.parameter.function, storage.modifier.package, storage.modifier.import, storage.type.java, variable.other */,
.pl-s .pl-s1 /* string source */ {
  color: #333;
}

.pl-ent /* entity.name.tag */ {
  color: #63a35c;
}

.pl-k /* keyword, storage, storage.type */ {
  color: #a71d5d;
}

.pl-s /* string */,
.pl-pds /* punctuation.definition.string, string.regexp.character-class */,
.pl-s .pl-pse .pl-s1 /* string punctuation.section.embedded source */,
.pl-sr /* string.regexp */,
.pl-sr .pl-cce /* string.regexp constant.character.escape */,
.pl-sr .pl-sre /* string.regexp source.ruby.embedded */,
.pl-sr .pl-sra /* string.regexp string.regexp.arbitrary-repitition */ {
  color: #183691;
}

.pl-v /* variable */ {
  color: #ed6a43;
}

.pl-id /* invalid.deprecated */ {
  color: #b52a1d;
}

.pl-ii /* invalid.illegal */ {
  color: #f8f8f8;
  background-color: #b52a1d;
}

.pl-sr .pl-cce /* string.regexp constant.character.escape */ {
  font-weight: bold;
  color: #63a35c;
}

.pl-ml /* markup.list */ {
  color: #693a17;
}

.pl-mh /* markup.heading */,
.pl-mh .pl-en /* markup.heading entity.name */,
.pl-ms /* meta.separator */ {
  font-weight: bold;
  color: #1d3e81;
}

.pl-mq /* markup.quote */ {
  color: #008080;
}

.pl-mi /* markup.italic */ {
  font-style: italic;
  color: #333;
}

.pl-mb /* markup.bold */ {
  font-weight: bold;
  color: #333;
}

.pl-md /* markup.deleted, meta.diff.header.from-file */ {
  color: #bd2c00;
  background-color: #ffecec;
}

.pl-mi1 /* markup.inserted, meta.diff.header.to-file */ {
  color: #55a532;
  background-color: #eaffea;
}

.pl-mdr /* meta.diff.range */ {
  font-weight: bold;
  color: #795da3;
}

.pl-mo /* meta.output */ {
  color: #1d3e81;
}

/* michelle added to try to learn to understand geometric layouts */
/* Set up some rules to govern the grid */
.grid { display: block; clear: both; }
.grid::after { content: ""; display: table; clear: both; }

.grid .unit { float: left; width: 100%; padding: 10px; }

/* This ensures the outer gutters are equal to the (doubled) inner gutters. */
.grid .unit:first-child { padding-left: 20px; }

.grid .unit:last-child { padding-right: 20px; }

/* Nested grids already have padding though, so let's nuke it */
.unit .unit:first-child { padding-left: 0; }

.unit .unit:last-child { padding-right: 0; }

.unit .grid:first-child > .unit { padding-top: 0; }

.unit .grid:last-child > .unit { padding-bottom: 0; }

/* Let people nuke the gutters/padding completely in a couple of ways */
.no-gutters .unit, .unit.no-gutters { padding: 0 !important; }

.grid .whole { width: 100%; }

.grid .half { width: 50%; }

.grid .one-third { width: 33.3332%; }

.grid .two-thirds { width: 66.6665%; }

.grid .one-quarter, .grid .one-fourth { width: 25%; }

.grid .three-quarters, .grid .three-fourths { width: 75%; }

.grid .one-fifth { width: 20%; }

.grid .two-fifths { width: 40%; }

.grid .three-fifths { width: 60%; }

.grid .four-fifths { width: 80%; }

.grid .golden-small { width: 38.2716%; }

.grid .golden-large { width: 61.7283%; }


/*! normalize.css v3.0.2 | MIT License | git.io/normalize */

/**
 * 1. Set default font family to sans-serif.
 * 2. Prevent iOS text size adjust after orientation change, without disabling
 *    user zoom.
 */

html {
  font-family: sans-serif; /* 1 */
  -ms-text-size-adjust: 100%; /* 2 */
  -webkit-text-size-adjust: 100%; /* 2 */
}

/**
 * Remove default margin.
 */

body {
  margin: 0;
}

/* HTML5 display definitions
   ========================================================================== */

/**
 * Correct `block` display not defined for any HTML5 element in IE 8/9.
 * Correct `block` display not defined for `details` or `summary` in IE 10/11
 * and Firefox.
 * Correct `block` display not defined for `main` in IE 11.
 */

article,
aside,
details,
figcaption,
figure,
footer,
header,
hgroup,
main,
menu,
nav,
section,
summary {
  display: block;
}

/**
 * 1. Correct `inline-block` display not defined in IE 8/9.
 * 2. Normalize vertical alignment of `progress` in Chrome, Firefox, and Opera.
 */

audio,
canvas,
progress,
video {
  display: inline-block; /* 1 */
  vertical-align: baseline; /* 2 */
}

/**
 * Prevent modern browsers from displaying `audio` without controls.
 * Remove excess height in iOS 5 devices.
 */

audio:not([controls]) {
  display: none;
  height: 0;
}

/**
 * Address `[hidden]` styling not present in IE 8/9/10.
 * Hide the `template` element in IE 8/9/11, Safari, and Firefox < 22.
 */

[hidden],
template {
  display: none;
}

/* Links
   ========================================================================== */

/**
 * Remove the gray background color from active links in IE 10.
 */

a {
  background-color: transparent;
}

/**
 * Improve readability when focused and also mouse hovered in all browsers.
 */

a:active,
a:hover {
  outline: 0;
}

/* Text-level semantics
   ========================================================================== */

/**
 * Address styling not present in IE 8/9/10/11, Safari, and Chrome.
 */

abbr[title] {
  border-bottom: 1px dotted;
}

/**
 * Address style set to `bolder` in Firefox 4+, Safari, and Chrome.
 */

b,
strong {
  font-weight: bold;
}

/**
 * Address styling not present in Safari and Chrome.
 */

dfn {
  font-style: italic;
}

/**
 * Address variable `h1` font-size and margin within `section` and `article`
 * contexts in Firefox 4+, Safari, and Chrome.
 */

h1 {
  font-size: 2em;
  margin: 0.67em 0;
}

/**
 * Address styling not present in IE 8/9.
 */

mark {
  background: #ff0;
  color: #000;
}

/**
 * Address inconsistent and variable font size in all browsers.
 */

small {
  font-size: 80%;
}

/**
 * Prevent `sub` and `sup` affecting `line-height` in all browsers.
 */

sub,
sup {
  font-size: 75%;
  line-height: 0;
  position: relative;
  vertical-align: baseline;
}

sup {
  top: -0.5em;
}

sub {
  bottom: -0.25em;
}

/* Embedded content
   ========================================================================== */

/**
 * Remove border when inside `a` element in IE 8/9/10.
 */

img {
  border: 0;
}

/**
 * Correct overflow not hidden in IE 9/10/11.
 */

svg:not(:root) {
  overflow: hidden;
}

/* Grouping content
   ========================================================================== */

/**
 * Address margin not present in IE 8/9 and Safari.
 */

figure {
  margin: 1em 40px;
}

/**
 * Address differences between Firefox and other browsers.
 */

hr {
  box-sizing: content-box;
  height: 0;
}

/**
 * Contain overflow in all browsers.
 */

pre {
  overflow: auto;
}

/**
 * Address odd `em`-unit font size rendering in all browsers.
 */

code,
kbd,
pre,
samp {
  font-family: monospace, monospace;
  font-size: 1em;
}

/* Forms
   ========================================================================== */

/**
 * Known limitation: by default, Chrome and Safari on OS X allow very limited
 * styling of `select`, unless a `border` property is set.
 */

/**
 * 1. Correct color not being inherited.
 *    Known issue: affects color of disabled elements.
 * 2. Correct font properties not being inherited.
 * 3. Address margins set differently in Firefox 4+, Safari, and Chrome.
 */

button,
input,
optgroup,
select,
textarea {
  color: inherit; /* 1 */
  font: inherit; /* 2 */
  margin: 0; /* 3 */
}

/**
 * Address `overflow` set to `hidden` in IE 8/9/10/11.
 */

button {
  overflow: visible;
}

/**
 * Address inconsistent `text-transform` inheritance for `button` and `select`.
 * All other form control elements do not inherit `text-transform` values.
 * Correct `button` style inheritance in Firefox, IE 8/9/10/11, and Opera.
 * Correct `select` style inheritance in Firefox.
 */

button,
select {
  text-transform: none;
}

/**
 * 1. Avoid the WebKit bug in Android 4.0.* where (2) destroys native `audio`
 *    and `video` controls.
 * 2. Correct inability to style clickable `input` types in iOS.
 * 3. Improve usability and consistency of cursor style between image-type
 *    `input` and others.
 */

button,
html input[type="button"], /* 1 */
input[type="reset"],
input[type="submit"] {
  -webkit-appearance: button; /* 2 */
  cursor: pointer; /* 3 */
}

/**
 * Re-set default cursor for disabled elements.
 */

button[disabled],
html input[disabled] {
  cursor: default;
}

/**
 * Remove inner padding and border in Firefox 4+.
 */

button::-moz-focus-inner,
input::-moz-focus-inner {
  border: 0;
  padding: 0;
}

/**
 * Address Firefox 4+ setting `line-height` on `input` using `!important` in
 * the UA stylesheet.
 */

input {
  line-height: normal;
}

/**
 * It's recommended that you don't attempt to style these elements.
 * Firefox's implementation doesn't respect box-sizing, padding, or width.
 *
 * 1. Address box sizing set to `content-box` in IE 8/9/10.
 * 2. Remove excess padding in IE 8/9/10.
 */

input[type="checkbox"],
input[type="radio"] {
  box-sizing: border-box; /* 1 */
  padding: 0; /* 2 */
}

/**
 * Fix the cursor style for Chrome's increment/decrement buttons. For certain
 * `font-size` values of the `input`, it causes the cursor style of the
 * decrement button to change from `default` to `text`.
 */

input[type="number"]::-webkit-inner-spin-button,
input[type="number"]::-webkit-outer-spin-button {
  height: auto;
}

/**
 * 1. Address `appearance` set to `searchfield` in Safari and Chrome.
 * 2. Address `box-sizing` set to `border-box` in Safari and Chrome
 *    (include `-moz` to future-proof).
 */

input[type="search"] {
  -webkit-appearance: textfield; /* 1 */ /* 2 */
  box-sizing: content-box;
}

/**
 * Remove inner padding and search cancel button in Safari and Chrome on OS X.
 * Safari (but not Chrome) clips the cancel button when the search input has
 * padding (and `textfield` appearance).
 */

input[type="search"]::-webkit-search-cancel-button,
input[type="search"]::-webkit-search-decoration {
  -webkit-appearance: none;
}

/**
 * Define consistent border, margin, and padding.
 */

fieldset {
  border: 1px solid #c0c0c0;
  margin: 0 2px;
  padding: 0.35em 0.625em 0.75em;
}

/**
 * 1. Correct `color` not being inherited in IE 8/9/10/11.
 * 2. Remove padding so people aren't caught out if they zero out fieldsets.
 */

legend {
  border: 0; /* 1 */
  padding: 0; /* 2 */
}

/**
 * Remove default vertical scrollbar in IE 8/9/10/11.
 */

textarea {
  overflow: auto;
}

/**
 * Don't inherit the `font-weight` (applied by a rule above).
 * NOTE: the default cannot safely be changed in Chrome and Safari on OS X.
 */

optgroup {
  font-weight: bold;
}

/* Tables
   ========================================================================== */

/**
 * Remove most spacing between table cells.
 */

table {
  border-collapse: collapse;
  border-spacing: 0;
}

td,
th {
  padding: 0;
}


* {
  box-sizing: border-box; }

body {
  padding: 0;
  margin: 0;
  font-family: "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 16px;
  line-height: 1.5;
  color: #606c71; }

a {
  color: #1e6bb8;
  text-decoration: none; }
  a:hover {
    text-decoration: underline; }

.btn {
  position: relative;
  display: inline-block;
  margin-bottom: 1rem;
  color: rgba(255, 255, 255, 0.7);
  background-color: rgba(255, 255, 255, 0.08);
  border-color: rgba(255, 255, 255, 0.2);
  border-style: solid;
  border-width: 1px;
  border-radius: 0.3rem;
  transition: color 0.2s, background-color 0.2s, border-color 0.2s; }
  .btn + .btn {
    margin-left: 1rem; }
    
.home-page-header .btn {
    display: block; }

.btn:hover {
  color: rgba(255, 255, 255, 0.8);
  text-decoration: none;
  background-color: rgba(255, 255, 255, 0.2);
  border-color: rgba(255, 255, 255, 0.3); }

@media screen and (min-width: 64em) {
  .btn {
    padding: 0.75rem 1rem; } }

@media screen and (min-width: 42em) and (max-width: 64em) {
  .btn {
    padding: 0.6rem 0.9rem;
    font-size: 0.9rem; } }

@media screen and (max-width: 42em) {
  .profilePicture {display:none;}
  .grid .one-third {display:none;}
  .grid .two-thirds {padding:0px;}
  .project-name {display:none}
  .btn {
    display: block;
    width: 100%;
    margin-left: 25%;
    padding: 0.75rem;
    font-size: 0.9rem; }
    .btn + .btn {
      margin-top: 1rem;
      margin-left: 25%; } }

.home-page-header {
  color: #fff;
  text-align: center;
  background-color: #159957;
  background-image: linear-gradient(120deg, #155799, #159957); }

.page-header {
  color: #fff;
  text-align: center;
  background-color: #159957;
  background-image: linear-gradient(120deg, #155799, #159957); }

@media screen and (min-width: 64em) {
  .page-header {
    padding: 5rem 6rem; } }

@media screen and (min-width: 42em) and (max-width: 64em) {
  .page-header {
    padding: 3rem 4rem; } }

@media screen and (max-width: 42em) {
  .page-header {
    padding: 2rem 1rem; } }

.project-name {
  margin-top: 0;
  margin-bottom: 0.1rem; }

@media screen and (min-width: 64em) {
  .project-name {
    font-size: 3.25rem; } }

@media screen and (min-width: 42em) and (max-width: 64em) {
  .project-name {
    font-size: 2.25rem; } }

@media screen and (max-width: 42em) {
  .project-name {
    font-size: 1.75rem; } }

.project-tagline {
  margin-bottom: 2rem;
  font-weight: normal;
  opacity: 0.7; }

@media screen and (min-width: 64em) {
  .project-tagline {
    font-size: 1.25rem; } }

@media screen and (min-width: 42em) and (max-width: 64em) {
  .project-tagline {
    font-size: 1.15rem; } }

@media screen and (max-width: 42em) {
  .project-tagline {
    font-size: 1rem; } }

.main-content :first-child {
  margin-top: 0; }
.main-content img {
  max-width: 100%; }
.main-content h1, .main-content h2, .main-content h3, .main-content h4, .main-content h5, .main-content h6 {
  margin-top: 2rem;
  margin-bottom: 1rem;
  font-weight: normal;
  color: #159957; }
.main-content p {
  margin-bottom: 1em; }
.main-content code {
  padding: 2px 4px;
  font-family: Consolas, "Liberation Mono", Menlo, Courier, monospace;
  font-size: 0.9rem;
  color: #383e41;
  background-color: #f3f6fa;
  border-radius: 0.3rem; }
.main-content pre {
  padding: 0.8rem;
  margin-top: 0;
  margin-bottom: 1rem;
  font: 1rem Consolas, "Liberation Mono", Menlo, Courier, monospace;
  color: #567482;
  word-wrap: normal;
  background-color: #f3f6fa;
  border: solid 1px #dce6f0;
  border-radius: 0.3rem; }
  .main-content pre > code {
    padding: 0;
    margin: 0;
    font-size: 0.9rem;
    color: #567482;
    word-break: normal;
    white-space: pre;
    background: transparent;
    border: 0; }
.main-content .highlight {
  margin-bottom: 1rem; }
  .main-content .highlight pre {
    margin-bottom: 0;
    word-break: normal; }
.main-content .highlight pre, .main-content pre {
  padding: 0.8rem;
  overflow: auto;
  font-size: 0.9rem;
  line-height: 1.45;
  border-radius: 0.3rem; }
.main-content pre code, .main-content pre tt {
  display: inline;
  max-width: initial;
  padding: 0;
  margin: 0;
  overflow: initial;
  line-height: inherit;
  word-wrap: normal;
  background-color: transparent;
  border: 0; }
  .main-content pre code:before, .main-content pre code:after, .main-content pre tt:before, .main-content pre tt:after {
    content: normal; }
.main-content ul, .main-content ol {
  margin-top: 0; }
.main-content blockquote {
  padding: 0 1rem;
  margin-left: 0;
  color: #819198;
  border-left: 0.3rem solid #dce6f0; }
  .main-content blockquote > :first-child {
    margin-top: 0; }
  .main-content blockquote > :last-child {
    margin-bottom: 0; }
.main-content table {
  display: block;
  width: 100%;
  overflow: auto;
  word-break: normal;
  word-break: keep-all; }
  .main-content table th {
    font-weight: bold; }
  .main-content table th, .main-content table td {
    padding: 0.5rem 1rem;
    border: 1px solid #e9ebec; }
.main-content dl {
  padding: 0; }
  .main-content dl dt {
    padding: 0;
    margin-top: 1rem;
    font-size: 1rem;
    font-weight: bold; }
  .main-content dl dd {
    padding: 0;
    margin-bottom: 1rem; }
.main-content hr {
  height: 2px;
  padding: 0;
  margin: 1rem 0;
  background-color: #eff0f1;
  border: 0; }

p.lisub {
  font-size: 0.9rem; }

@media screen and (min-width: 64em) {
  .main-content {
    max-width: 64rem;
    padding: 2rem 6rem;
    margin: 0 auto;
    font-size: 1.1rem; } }

@media screen and (min-width: 42em) and (max-width: 64em) {
  .main-content {
    padding: 2rem 4rem;
    font-size: 1.1rem; } }

@media screen and (max-width: 42em) {
  .main-content {
    padding: 2rem 1rem;
    font-size: 1rem; } }

.site-footer {
  padding-top: 2rem;
  margin-top: 2rem;
  border-top: solid 1px #eff0f1; }

.site-footer-owner {
  display: block;
  font-weight: bold; }

.site-footer-credits {
  color: #819198; }

@media screen and (min-width: 64em) {
  .site-footer {
    font-size: 1rem; } }

@media screen and (min-width: 42em) and (max-width: 64em) {
  .site-footer {
    font-size: 1rem; } }

@media screen and (max-width: 42em) {
  .site-footer {
    font-size: 0.9rem; } }

</style>
""", unsafe_allow_html=True)