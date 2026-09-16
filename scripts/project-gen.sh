#!/bin/sh

USERNAME="wak6817"
YEAR=$(date +%Y)

printf "Are you running this script in the project directory? (y/n) "
read -r answer

if [ "$answer" = "y" ]; then
    echo "Continue"

    #TODO: Write this tutorial and copy it to README.md
    cat > README.md <<EOF
This tutorial is not written yet...
EOF

    echo "Generated README.md"

    cat > LICENSE.md <<EOF
MIT License

Copyright (c) $YEAR $USERNAME

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
EOF

    echo "Generated LICENSE"

    cat > .gitignore <<EOF
.DS_Store
EOF

    echo "Generated .gitignore"

    mkdir -p src
    echo "Generated src/"

    mkdir -p assets/fonts assets/icons assets/soundsx
    echo "Generated assets/"

    mkdir -p scripts
    echo "Generated scripts/"

    cat > scripts/run.sh <<EOF
#!/bin/sh
cp -R src assets scripts page dist/
EOF

  echo "Generated scripts/run.sh"


    mkdir -p page
    touch page/index.html page/style.css page/script.ts
    echo "Generated page/"

    mkdir -p dist
    echo "Generated dist/"

    if command -v npm >/dev/null 2>&1; then
        npm init -y
        npm install --save-dev typescript

        echo "Installed TypeScript using npm"
    else
        echo "Warning: npm was not found."
        echo "Go to your Web_StaticY installation and run the scripts/download/<os-pkg>.sh script"
    fi

    printf "\nThis could take a few seconds!\n"
else
    echo "Abort"
fi