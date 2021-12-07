import java.util.Properties;

public class PropertiesEx {
    public static void main(String[] args) {
        Properties sysProp = System.getProperties();

        sysProp.list(System.out);
    }
}
