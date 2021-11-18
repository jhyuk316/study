import java.util.ArrayList;

import models.*;

/**
 * BasicsJava
 */
public class BasicsJava {

    public static void main(String[] args) {
        Person person = new Person("홍길동", 34);

        System.out.println(person);

        Hero hero1 = new Hero("슈퍼맨");
        Hero hero2 = new Hero("배트맨");

        hero1.attack(hero2);
        hero1.attack(person);

        Chara hero4 = new Hero();        
        ICharacters hero5 = new Hero();


        hero4.attack(hero1);
        hero5.attack(person);

        if (hero4 instanceof Hero){
            System.out.println("영웅이다");
        }
        if (hero4 instanceof Person){
            System.out.println("인간이다");
        }
        if (hero4 instanceof Chara){
            System.out.println("캐릭터이다");
        }

        ArrayList<Chara> charaList = new ArrayList<>();
        charaList.add(hero1);
        charaList.add(hero4);
        //charaList.add(hero5); ERROR chara의 범위를 벗어남

        print("String");
        print(1);
        print(3.3f);

        new Thread(new Runnable() {
            @Override
            public void run() {
                for(int i = 0; i<5;++i){
                    try {
                        Thread.sleep(300);
                        System.out.println(Thread.currentThread().getName() + ":" + i);
                    } catch (Exception e) {
                        e.printStackTrace();
                    }
                }
            }
        }).start();;

        new Thread(() -> {
            for(int i = 0; i<5;++i){
                try {
                    Thread.sleep(300);
                    System.out.println(Thread.currentThread().getName() + ":" + i);
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        }).start();;
       
    }

    public static <T> void print(T type) {
        System.out.println(type);
    }
}