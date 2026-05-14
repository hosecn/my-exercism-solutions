public class Lasagna {
    public int expectedMinutesInOven() {
        return 40;
    }
    public int remainingMinutesInOven(int passedTime) {
        return 40 - passedTime;
    }
    public int preparationTimeInMinutes(int layerNumber) {
        return 2 * layerNumber;
    }
    public int totalTimeInMinutes(int layerNumber, int passedTime) {
        return passedTime + preparationTimeInMinutes(layerNumber);
    }
}
