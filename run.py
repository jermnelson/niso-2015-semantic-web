__author__ = "Jeremy Nelson"

import argparse
import jinja2
import os

ENV = jinja2.Environment(
        loader=jinja2.PackageLoader("presentation", "templates"))
OUTPUT_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                         "dist")
print(OUTPUT_DIR)

def render_templates():
    for template_name in ["index.html", 
        "about.html",
        "bibframe-overview.html",
        "bibcat.html",
        "bibframe-2.0.html",
        "languages.html",
        "identifiers.html",
        "sparql.html",
        "summary.html"]:
        template = ENV.get_template(template_name)
        with open(os.path.join(OUTPUT_DIR, template_name),
                  "w+") as raw_file:
            raw_file.write(template.render())


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("render", default=True)
    args = parser.parse_args()
    if args.render:
        render_templates()
