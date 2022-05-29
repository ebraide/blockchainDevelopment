// SPDX-License-Identifier: MIT
pragma solidity >=0.6.0 <0.9.0;

contract helloWorld{
  string public message;

  constructor(string memory initialMessage){
    message = initialMessage;
  }

  function updateMessage(string memory newMessage) public {
    message = newMessage;
  }
}
