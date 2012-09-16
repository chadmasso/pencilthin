# pencilthin #
## Prerequisites ##

- handlebars node precompiler (http://handlebarsjs.com/precompilation.html)

## Installation ##
### Install the package ###
pip coming soon...

#### Configure your settings ####
coming soon...

### Goal ###
I would like to precompile handlebar templates into a javascript file on the server side when I change one of my handlebar templates. I would also like to use django template tags such as {% url %} and {% static %} in these handlebar templates.

### Proof of Concept ###
I have been able to (currently very sloppy, messy, hacky) create a precompile management command that pulls all handlebar templates from a specific directory, precompiles them, correctly handles django template tags and outputs to a minified javascript file.

#### Example ####
An example handlebars template

    {% load static from staticfiles %}

    <img src="{% static 'a.png' %}" />

    <p>Hello {{ name }}!</p>

    <p>Go <a href='{% url home %}'>home</a>!</p>

compiles into

    (function(){var a=Handlebars.template,b=Handlebars.templates=Handlebars.templates||{};b["a.bar"]=a(function(a,b,c,d,e){c=c||a.helpers;var f="",g,h,i="function",j=this.escapeExpression;return f+="\n\n<img src="/static/a.png" />\n\n<p>Hello ",h=c.name,h?g=h.call(b,{hash:{}}):(g=b.name,g=typeof g===i?g():g),f+=j(g)+"!</p>\n\n<p>Go <a href='/'>home</a>!</p>",f})})()
