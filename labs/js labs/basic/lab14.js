function pick6 () {
    let ticket = [];
    for (let i = 0; i < 6; i++) {
        ticket[i] = Math.floor((Math.random() * 100) + 1)
    }
    return ticket
}

function matches (winningTicket, myTicket) {
    let counter = 0;

    for (let i = 0; i < winningTicket.length; i++) {
        if (winningTicket[i] === myTicket[i]) {
            counter += 1;
        }
    }
    if (counter === 0) {
        return 0
    }
    if (counter === 1) {
        console.log('Match 1: '+ myTicket);
        return 4
    }
    if (counter === 2) {
        console.log('Match 2 '+ myTicket);
        return 7
    }
    if (counter === 3) {
        console.log('Match 3: '+ myTicket);
        return 100
    }
    if (counter === 4) {
        console.log('Match 4: '+ myTicket);
        return 50000
    }
    if (counter === 5) {
        console.log('Match 5: '+ myTicket);
        return 1000000
    }
    if (counter === 6) {
        console.log('Match 6: '+ myTicket);
        return 25000000
    }
}

function playGame() {
    let spend = 0;
    let winnings = 0;
    let winner = pick6();
    console.log('Winning Ticket: ' + winner);

    for (let i = 0;i < 10; i++) {
        let my_ticket = pick6();
        winnings += matches(winner, my_ticket);
        spend += 2;
    }

    let result = ('You spent $' + spend + '. \nYou won $' + winnings + '.\n')
    return result
}

let result = playGame()

console.log(result)