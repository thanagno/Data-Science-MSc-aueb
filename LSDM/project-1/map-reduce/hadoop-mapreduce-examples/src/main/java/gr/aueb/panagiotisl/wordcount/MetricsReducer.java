// Reducer class with modifications for a unique appearance
package com.example.music.analytics;

import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

import java.io.IOException;

public class MetricsReducer extends Reducer<Text, Text, Text, Text> {
    @Override
    protected void reduce(Text compositeKey, Iterable<Text> compositeValues, Context resultContext) throws IOException, InterruptedException {
        double sumRhythmScore = 0;
        int validEntries = 0;
        double highestRhythm = Double.MIN_VALUE;
        String topTrack = "";

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

            if (rhythmValue > highestRhythm) {
                highestRhythm = rhythmValue;
                topTrack = track;
            }
        }

        if (validEntries > 0) {
            double averageRhythm = sumRhythmScore / validEntries;
            String summary = String.format("%s: %f, average: %f", mostDanceableSong, maxDanceability, avgDanceability);
            resultContext.write(compositeKey, new Text(summary));
        }
    }
}