package org.example;

// Reducer class with modifications for a unique appearance
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

import java.io.IOException;

public class CountReducer extends Reducer<Text, Text, Text, Text> {
    @Override
    protected void reduce(Text compositeKey, Iterable<Text> compositeValues, Context resultContext) throws IOException, InterruptedException {
        int validEntries = 0;
        double maxRhythm = Double.MIN_VALUE;
        String topTrack = "";
        double sumRhythmScore = 0;

        for (Text val : compositeValues) {
            String[] valueParts = val.toString().split("\\|\\|\\|", -1);

            if (valueParts.length < 2) continue;

            String track = valueParts[0];
            double rhythmValue;
            try {
                rhythmValue = Double.parseDouble(valueParts[1]);
            } catch (NumberFormatException e) {
                continue;
            }

            sumRhythmScore += rhythmValue;
            validEntries++;

            if (rhythmValue > maxRhythm) {
                maxRhythm = rhythmValue;
                topTrack = track;
            }
        }

        if (validEntries > 0) {
            double avgRythm = sumRhythmScore / validEntries;
            String summary = String.format("%s: %f, average: %f", topTrack, maxRhythm, avgRythm);
            resultContext.write(compositeKey, new Text(summary));
        }
    }
}