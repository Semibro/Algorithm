function solution(phone_book) {
    const answer = true;
    const phoneBook = phone_book;
    phoneBook.sort();
    
    for (let index = 0; index < phoneBook.length - 1; index++) {
        const current = phoneBook[index];
        const next = phoneBook[index + 1];
        
        if (next.startsWith(current)) {
            return false;
        }
    }
    
    return true;
}