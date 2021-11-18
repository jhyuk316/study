package models;

public class Hero extends Chara implements ICharacters {
    public Hero() {
        super();
    }

    public Hero(String name) {
        setName(name);
    }

    @Override
    public void attack(Chara character) {
        System.out.println(this.getName() + "은 " + character.getName() + "과 싸운다");
    }

    @Override
    public void attack(Person person) {
        System.out.println(this.getName() + "은 " + person.getName() + "을 공격 할 수 밖에 없었다.");
    }
}
