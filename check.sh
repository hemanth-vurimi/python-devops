#!/bin/bash

f1(){

    read -p "Enter your name: " name
    echo "Name is $name"

}

f2(){

    f1 = $1
    f2 = $2

    addition = $((${f1} +  ${f2}))
}

f1