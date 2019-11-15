#!/bin/bash

mkdir templates/documentation
pydoc3 -w data
pydoc3 -w fitting
pydoc3 -w visualize
mv *.html templates/documentation
