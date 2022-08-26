//println!("NOP");
pub fn parsing(eq: String) {
    //check available character
    eq.chars().for_each(|x| {
        if available_char(x) == false {
            //error message
        }
    });
    if basic_check(eq.clone()) == false {
        //error message
    }
    //specefic check in a loop
    let mut eq_vec: Vec<char> = eq.chars().collect();
    eq_vec = space_formatting(eq_vec.clone());
    println!("{:?}", eq_vec);
 //   check_operator_ordering(eq_vec);
    for (i, c) in eq_vec.iter().enumerate() {
        check_x_format(eq_vec.clone(), *c, i);
        check_decimal_format(eq_vec.clone(), *c, i);
    }
}

fn space_formatting(eq_vec: Vec<char>) -> Vec<char> {
    let mut ret = Vec::new();
    for (i, c) in eq_vec.iter().enumerate() {
        if *c != ' ' {
            ret.push(*c);
        }
        if c.is_digit(10) == true {
            match eq_vec.get(i + 1) {
                Some(x) => {
                    if x.is_digit(10) == false {
                        ret.push(' ');
                    }
                },
                _ => ()
            }
        } else if *c != ' ' {
            ret.push(' ');
        }
    }
    ret
}
/*
fn check_operator_ordering(eq_vec: Vec<char>) {
    for (i, c) in eq_vec.split(|x| *x == ' ').enumerate() {
        if i % 2 == 1 {
            if is_operator(*c) == false {
                //error message
                println!("NOP");
            }
        } else {
            if is_operator(*c) == true {
                //error message
                println!("NOP");
            }
        }
    }
}
*/
fn check_x_format(eq_vec: Vec<char>, c: char, i: usize) {
    if c == 'X' {
        if i > 0 {
            match eq_vec.get(i - 1) {
                Some(x) => {
                    if *x == '^' {
                        //error message
                        println!("NOP");
                    }
                }
                _ => {
                    //error message
                    println!("NOP");
                }
            }
        }
        match eq_vec.get(i + 1) {
            Some(x) => {
                if *x != '^' {
                    //error message
                    println!("NOP");
                } else {
                    match eq_vec.get(i + 2) {
                        Some(y) => {
                            if y.is_digit(10) == false {
                                //error message
                                println!("NOP");
                            }
                        },
                        _ => {
                            //error message
                            println!("NOP");}
                    }
                }
            },
            _ => {
                //error message
                println!("NOP");}
        }
    }
}

fn check_decimal_format(eq_vec: Vec<char>, c: char, i: usize) {
    if c == '.' {
        if i > 0 {
            match eq_vec.get(i - 1) {
                Some(x) => {
                    if x.is_digit(10) == false {
                        //error message
                        println!("NOP");
                    }
                },
                _ => {
                    //error message
                    println!("NOP");}
            }
        } else {
            //error message
            println!("NOP");
        }
        match eq_vec.get(i + 1) {
            Some(x) => {
                if x.is_digit(10) == false {
                    //error message
                    println!("NOP");
                }
            },
            _ => {
                //error message
                println!("NOP");}
        }
    }
}

fn is_operator(c: char) -> bool {
    match c {
        '+' => true,
        '-' => true,
        '*' => true,
        '/' => true,
        '^' => true,
        '=' => true,
        _ => false
    }
}


fn available_char(c: char) -> bool {
    match c {
        '+' => true,
        '-' => true,
        '*' => true,
        '/' => true,
        '^' => true,
        '.' => true,
        '=' => true,
        'X' => true,
        'x' => true,
        ' ' => true,
        _ => c.is_digit(10)
    }
}


fn basic_check(eq: String) -> bool {
    //check equal's number
    let mut equal_count = 0;
    eq.chars().for_each(|x| {
        if x == '=' {
            equal_count += 1;
        }
    });
    if equal_count != 1 {
        return false
    }

    true
}

