// Kotlin functions begin with keyword fun
// Kotlin applications entry point is main function

var matchCounter = 0
var myPhrase = " e"

fun main(args: Array<String>){

    println("Is Unique: implement an algorithm to determine if a string has all unique characters.\n")
    println("First test string: ")
    myPhrase = "This is my test phrase with duplicate characters"
    println(myPhrase)
    myPhrase.forEachIndexed { idx, e -> isUnique(myPhrase, idx, e) }
    printResult(matchCounter)

    println("Second test string: ")
    matchCounter = 0
    myPhrase = "23efghjubvs"
    println(myPhrase)
    myPhrase.forEachIndexed { idx, e -> isUnique(myPhrase, idx, e) }
    printResult(matchCounter)
}

fun isUnique(myString: String, index: Int, checkVal: Char) {
    myString.forEachIndexed {idx, c -> if(idx !== index) { if(c === myString[index]) { matchCounter++ }}}
}

fun printResult(counter: Int){
    if(counter > 0){
        println("The test string does not have all unique characters.\n")
    }
    else {
        println("The test string is made up of unique characters.\n")
    }
}

