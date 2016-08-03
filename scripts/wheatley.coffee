# Description:
#   Wheatley from Portal 2
#
# Dependencies:
#   None
#
# Configuration:
#
# Commands:
#   Say Wheatley - Wheatley reacts
#
# Author:
#   Thibaut Tauveron <thibaut.tauveron@gmail.com> (https://github.com/gnut3ll4)

list = require './data/list.json'

regex = /\bwheatley\b/i

module.exports = (robot) ->
  robot.hear regex, (msg) ->
    entry = msg.random list
    msg.send entry.url
