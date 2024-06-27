Feature: Interact with Windows Media Player Second milestone

  @seml @pause @FI @SI @QR @Priority_3-High @Type_functionality
  Scenario: Media functionality in full screen
    Given the Windows Media Player application is started
    When I click on the "Videos" tree item
    Then I click on the "Subtitles_sample_video"
    Then I click on the play button
    Then I "pause" the media playback
    Then I wait for 5 seconds
    Then I full screen the media playback
    Then I wait for 5 seconds
    Then the application should be interacted with successfully
    Then the application should be closed

  @seml @pause @FI @SI @QR @Priority_3-High @Type_functionality
  Scenario: Media resize functionality
    Given the Windows Media Player application is started
    When I click on the "Videos" tree item
    Then I click on the "Subtitles_sample_video"
    Then I click on the play button
    Then I "pause" the media playback
    Then I wait for 5 seconds
    Then I full screen the media playback
    Then I wait for 5 seconds
    Then I click on the escape button to resize media playback
    Then the application should be interacted with successfully
    Then the application should be closed

  @seml @pause @FI @SI @QR @Priority_3-High @Type_functionality
  Scenario: Media volume functionality check
    Given the Windows Media Player application is started
    When I click on the "Music" tree item
    Then I click on the "MP3_Sample_Files" list item
    Then I click on the play button
    Then I "pause" the media playback
    Then I wait for 5 seconds
    Then I move the volume slider to right
    Then I move the volume slider to left
    Then the application should be interacted with successfully
    Then the application should be closed

  @seml @pause @FI @SI @QR @Priority_3-High @Type_functionality
  Scenario: Sliding progress indicator
    Given the Windows Media Player application is started
    When I click on the "Music" tree item
    Then I click on the "MP3_Sample_Files" list item
    Then I click on the play button
    Then I wait for 2 seconds
    Then I "pause" the media playback
    Then I move the play seek slider to left
    Then I move the play seek slider to right
    Then the application should be interacted with successfully
    Then the application should be closed

  @seml @pause @FI @SI @QR @Priority_3-High @Type_functionality
  Scenario: Functionality of sliding bar
    Given the Windows Media Player application is started
    When I click on the "Videos" tree item
    Then I click on the "Subtitles_sample_video"
    Then I click on the play button
    Then I wait for 2 seconds
    Then I "pause" the media playback
    Then I move the play seek slider to right

  @seml @pause @FI @SI @QR @Priority_3-High @Type_functionality
  Scenario: Verify subtitle option in wmp
    Given the Windows Media Player application is started
    When I click on the "Videos" tree item
    Then I click on the "Subtitles_sample_video"
    Then I click on the play button
    Then I "pause" the media playback
    Then I wait for 5 seconds
    Then I full screen the media playback
    Then I wait for 5 seconds
    Then I press Ctrl+Shift+C to see subtitle options
    Then the application should be interacted with successfully
    Then the application should be closed

  @seml @pause @FI @SI @QR @Priority_3-High @Type_functionality
  Scenario: Verify subtitle option turn off
    Given the Windows Media Player application is started
    When I click on the "Videos" tree item
    Then I click on the "Subtitles_sample_video"
    Then I click on the play button
    Then I "pause" the media playback
    Then I wait for 5 seconds
    Then I press ALT+P, then press B then press F
    Then the application should be interacted with successfully
    Then the application should be closed
