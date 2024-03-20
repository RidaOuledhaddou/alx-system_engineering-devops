#!/usr/bin/env ruby

# A regular expression to extract sender, receiver, and flags
regex = /\[from:(.*?)\]\s\[to:(.*?)\]\s\[flags:(.*?)\]/

# Extracting sender, receiver, and flags from the input using the regular expression
matches = ARGV[0].scan(regex)

# Formatting the output
output = matches.map { |match| match.join(',') }.join("\n")

# Printing the result
puts output
