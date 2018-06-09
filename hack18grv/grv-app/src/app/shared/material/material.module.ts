import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { MatGridListModule } from '@angular/material/grid-list';
import { MatSliderModule } from '@angular/material/slider';
import { MatCardModule } from '@angular/material/card';

@NgModule({
  imports: [
    CommonModule,
    MatGridListModule,
    MatSliderModule,
    MatCardModule
  ],
  declarations: [],
  exports: [
    MatGridListModule,
    MatSliderModule,
    MatCardModule
  ]
})
export class MaterialModule { }
